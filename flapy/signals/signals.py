from PySide6.QtCore import Signal, QObject


class fSignals(QObject):
    """
    self.fsignals.clicked.connect() = fSignals(slot)
    """

    # Mouse events
    mouse_click = Signal()
    mouse_hover = Signal()
    mouse_leave = Signal()
    mouse_double_click = Signal()

    # Keyboard events
    ...

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.p = parent

        # built-in signals
        self.clicked = self._add_no_signal("clicked")
        self.pressed = self._add_no_signal("pressed")
        self.released = self._add_no_signal("released")
        self.text_changed = self._add_no_signal("textChanged")
    
    def _add_no_signal(self, 
                       signal_name: str, 
                       default: object = None) -> object:
        return getattr(self.p, signal_name, default)