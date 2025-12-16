"""Minimal UI window with background, overlay, and icon grid."""

from pathlib import Path
import random
from typing import Dict, List
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QGridLayout,
)
from PySide6.QtGui import QPixmap, QPainterPath, QRegion, QIcon, QShortcut, QKeySequence
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QSizePolicy

from .widgets import SoundButton

#This is where the mapping of the number pad keys to which sound is defined
DEFAULT_MAPPING: Dict[str, Dict[str, str]] = {
    "1": {"prefix": "laugh", "label": "LAUGH"},
    "2": {"prefix": "swamp", "label": "SWAMP"},
    "3": {"prefix": "alive", "label": "ALIVE"},
    "4": {"prefix": "i_am_music", "label": "I AM MUSIC"},
    "5": {"prefix": "swamp_izzo", "label": "SWAMP IZZO"},
    "6": {"prefix": "ha", "label": "HA"},
    "7": {"prefix": "what_up_baby_boy", "label": "BABY BOY"},
    "8": {"prefix": "snare", "label": "SNARE"},
    "9": {"prefix": "gunshot", "label": "GUNSHOT"},
}


class SoundboardWindow(QMainWindow):
    def __init__(self, assets_dir: Path):
        super().__init__()
        self.assets_dir = Path(assets_dir)
        self.ui_dir = self.assets_dir / "ui"
        self.audio_dir = self.assets_dir / "audio"
        self.mapping = DEFAULT_MAPPING
        self.buttons: Dict[str, SoundButton] = {}
        self.bg_label: QLabel | None = None
        self.grid_host: QWidget | None = None
        self.active_players: List[QMediaPlayer] = []

        self._setup_window()
        self._build_layers()

    def _setup_window(self) -> None:
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowTitleHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowCloseButtonHint
            | Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setFixedSize(640, 640)
        self.setWindowTitle("Swamp Izzo UI Preview")
        self.setWindowIcon(QIcon(str(self.ui_dir / "background_i_am_music.png")))
        self.setFocusPolicy(Qt.StrongFocus)
        self._apply_round_mask()
        self._setup_shortcuts()
        QTimer.singleShot(50, self._debug_log_sizes)

    def _build_layers(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)

        # Manual layering: background -> grid host.
        self.bg_label = QLabel(central)
        self.bg_label.setPixmap(QPixmap(str(self.ui_dir / "background_i_am_music.png")))
        self.bg_label.setScaledContents(True)

        self.grid_host = QWidget(central)
        self.grid_host.setAttribute(Qt.WA_StyledBackground, True)
        self.grid_host.setStyleSheet(
            "background-color: rgba(255, 255, 255, 15);"
            "border: 1px solid rgba(255, 255, 255, 80);"
            "border-radius: 18px;"
        )
        self.bg_label.lower()
        self.grid_host.raise_()

        grid_layout = QGridLayout(self.grid_host)
        grid_layout.setContentsMargins(32, 32, 32, 32)
        grid_layout.setSpacing(18)
        grid_layout.setAlignment(Qt.AlignCenter)
        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)
        grid_layout.setRowStretch(2, 1)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 1)

        sorted_keys = sorted(self.mapping.keys(), key=lambda k: int(k))
        for idx, key in enumerate(sorted_keys):
            prefix = self.mapping[key]["prefix"]
            label = self.mapping[key]["label"]
            icon_path = self._icon_for_prefix(prefix)
            btn = SoundButton(key, label, icon_path, self.ui_dir)
            btn.clicked.connect(lambda _=False, p=prefix: self._play_sound(p))
            self.buttons[key] = btn
            row, col = divmod(idx, 3)
            grid_layout.addWidget(btn, row, col, alignment=Qt.AlignCenter)

    def _debug_log_sizes(self) -> None:
        print(
            "[debug] sizes:",
            {
                "window": (self.width(), self.height()),
                "central": (
                    self.centralWidget().width() if self.centralWidget() else None,
                    self.centralWidget().height() if self.centralWidget() else None,
                ),
            },
            flush=True,
        )

    def _icon_for_prefix(self, prefix: str) -> Path:
        candidate = self.ui_dir / "icons" / f"icon_{prefix}.png"
        if candidate.exists():
            return candidate
        return self.ui_dir / "icons" / "icon_swamp.png"

    def _audio_folder_for_prefix(self, prefix: str) -> Path | None:
        overrides = {
            "what_up_baby_boy": "what_up",
        }
        folder_name = overrides.get(prefix, prefix)
        folder = self.audio_dir / folder_name
        return folder if folder.exists() and folder.is_dir() else None

    def _random_audio_path(self, prefix: str) -> Path | None:
        folder = self._audio_folder_for_prefix(prefix)
        if not folder:
            return None
        candidates = sorted(p for p in folder.glob("*.mp3") if p.is_file())
        if not candidates:
            return None
        return random.choice(candidates)

    def _play_sound(self, prefix: str) -> None:
        audio_path = self._random_audio_path(prefix)
        if not audio_path:
            return
        output = QAudioOutput(self)
        output.setVolume(0.9)
        player = QMediaPlayer(self)
        player.setAudioOutput(output)
        player.setSource(QUrl.fromLocalFile(str(audio_path)))

        # Track to allow overlap and clean up when done.
        self.active_players.append(player)
        player.playbackStateChanged.connect(
            lambda state, p=player: self._cleanup_player(p, state)
        )
        player.play()

    def _cleanup_player(self, player: QMediaPlayer, state: QMediaPlayer.PlaybackState) -> None:
        if state == QMediaPlayer.PlaybackState.StoppedState and player in self.active_players:
            self.active_players.remove(player)
            player.deleteLater()

    def resizeEvent(self, event) -> None:  # type: ignore[override]
        super().resizeEvent(event)
        if self.centralWidget() is None:
            return
        rect = self.centralWidget().rect()
        if self.bg_label:
            self.bg_label.setGeometry(rect)
        if self.grid_host:
            self.grid_host.setGeometry(rect)

    def _apply_round_mask(self) -> None:
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 20, 20)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def _setup_shortcuts(self) -> None:
        QShortcut(QKeySequence("Ctrl+Q"), self, activated=self.close)
        QShortcut(QKeySequence("Meta+Q"), self, activated=self.close)
        QShortcut(QKeySequence(Qt.Key_Escape), self, activated=self.close)

    def keyPressEvent(self, event) -> None:  # type: ignore[override]
        if event.isAutoRepeat():
            return
        key = self._key_from_event(event)
        if key and key in self.buttons:
            self.buttons[key].setDown(True)
            prefix = self.mapping.get(key, {}).get("prefix")
            if prefix:
                self._play_sound(prefix)
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event) -> None:  # type: ignore[override]
        if event.isAutoRepeat():
            return
        key = self._key_from_event(event)
        if key and key in self.buttons:
            self.buttons[key].setDown(False)
        super().keyReleaseEvent(event)

    def _key_from_event(self, event) -> str | None:
        key_map = {
            Qt.Key_1: "7",
            Qt.Key_2: "8",
            Qt.Key_3: "9",
            Qt.Key_4: "4",
            Qt.Key_5: "5",
            Qt.Key_6: "6",
            Qt.Key_7: "1",
            Qt.Key_8: "2",
            Qt.Key_9: "3",
        }
        return key_map.get(event.key())
