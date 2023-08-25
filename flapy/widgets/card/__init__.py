from PySide6.QtWidgets import QWidget, QLayout, QGridLayout
from PySide6.QtCore import Qt
from typing import Tuple, Callable, Any
from ...common import Base
from ...signals import SignalType


class Card(Base, QWidget):
    def __init__(self, 
                 child: QWidget,
                 id: str = None,
                 signals: list[Tuple[SignalType, Callable[..., Any]]] = None,
                 **kwargs) -> None:
        QWidget.__init__(self)
        Base.__init__(self, id, signals, **kwargs)

        self.child = child
        self._set_widget(child)

    def _set_widget(self, widget: QWidget) -> None:
        if isinstance(widget, QWidget):
            self._layout = QGridLayout(self)
            self._layout.addWidget(widget, 0, 0, Qt.AlignmentFlag.AlignCenter)
        elif isinstance(widget, QLayout):
            self.setLayout(widget)
    
    def _rebuild(self):
        self.deleteLater()
        self._set_widget(self.child)