from PySide6.QtCore import Signal, QObject


class fSignals(QObject):

    # Mouse events
    mouseClick = Signal()
    mouseHover = Signal()
    mouseLeave = Signal()
    mouseDoubleClick = Signal()

    # Keyboard events
    ...

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.p = parent

    def _getattr(self, name: str, default: object = None) -> object:
        return getattr(self, name, getattr(self.p, name, default))
