from PySide6.QtWidgets import QLineEdit
from typing import Tuple, Callable, Any
from ...common.base import Base
from ...signals import SignalType


class LineEdit(Base, QLineEdit):
    def __init__(self, 
                 id: str = None,
                 text: str = "",
                 placeholder: str = None,
                 signals: list[Tuple[SignalType, Callable[..., Any]]] = None,
                 **kwargs):

        QLineEdit.__init__(self)
        Base.__init__(self, id, signals, **kwargs)

        self._set_text(text)
        self._set_placeholder(placeholder)

    def _set_text(self, text: str):
        if text is not None:
            self.setText(text)

    def _set_placeholder(self, text: str):
        if text is not None:
            self.setPlaceholderText(text)