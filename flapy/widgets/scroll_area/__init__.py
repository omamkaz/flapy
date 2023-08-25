from PySide6.QtWidgets import QScrollArea, QWidget, QLayout
from typing import Tuple, Callable, Any
from ...common.base import Base
from ...signals import SignalType


class ScrollArea(Base, QScrollArea):
    def __init__(self, 
                 child: QWidget,
                 id: str = None,
                 signals: list[Tuple[SignalType, Callable[..., Any]]] = None,
                 widget_resizable: bool = None,
                 **kwargs) -> None:
        QScrollArea.__init__(self)
        Base.__init__(self, id, signals, **kwargs)

        self.child = child
        self._set_widget_resizable(widget_resizable)
        self._set_widget(child)

    def _set_widget_resizable(self, widget_resizable: bool) -> None:
        if widget_resizable is not None:
            self.setWidgetResizable(widget_resizable)

    def _set_widget(self, widget: QWidget) -> None:
        if isinstance(widget, QWidget):
            self.setWidget(widget)
        elif isinstance(widget, QLayout):
            self.setLayout(widget)

    # def _rebuild(self):
    #     if isinstance(self.child, QWidget):
    #         self.widget().deleteLater()
    #     elif isinstance(self.child, QLayout):
    #         self.layout().deleteLater()

    #     # self._set_widget(self.child)