"""UI widgets for the soundboard preview."""

from pathlib import Path
from PySide6.QtWidgets import QToolButton, QSizePolicy
from PySide6.QtGui import QIcon, QPixmap, QFont, QCursor
from PySide6.QtCore import Qt, QSize


class SoundButton(QToolButton):
    """Button that shows an icon and label with custom skins."""

    def __init__(self, key: str, label: str, icon_path: Path, assets_path: Path):
        super().__init__()
        self.key = key
        self.assets_path = Path(assets_path)
        self.icon_path = Path(icon_path)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setCheckable(False)
        self.setAutoRaise(False)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(QSize(150, 150))

        font = QFont()
        font.setPointSize(11)
        font.setWeight(QFont.Weight.DemiBold)
        self.setFont(font)
        self.setText("")

        self._apply_icon()
        self._apply_stylesheet()

    def _apply_icon(self) -> None:
        pixmap = QPixmap(str(self.icon_path))
        if not pixmap.isNull():
            scaled = pixmap.scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setIcon(QIcon(scaled))
            self.setIconSize(QSize(128, 128))

    def _apply_stylesheet(self) -> None:
        default_img = self.assets_path / "button_default.png"
        hover_img = self.assets_path / "button_hover.png"
        pressed_img = self.assets_path / "button_pressed.png"

        self.setStyleSheet(
            f"""
            QToolButton {{
                qproperty-iconSize: 128px 128px;
                qproperty-toolButtonStyle: ToolButtonIconOnly;
                background: transparent;
                border: none;
                padding: 0;
            }}
            QToolButton:hover {{
                background: transparent;
            }}
            QToolButton:pressed {{
                background: transparent;
            }}
            """
        )
