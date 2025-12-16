"""App entrypoint for UI-only preview."""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from .ui.main_window import SoundboardWindow


def main() -> None:
    assets_dir = Path(__file__).resolve().parent.parent / "assets"
    app = QApplication(sys.argv)
    window = SoundboardWindow(assets_dir)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
