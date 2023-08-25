from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QToolBar,
    QStatusBar,
    QDockWidget,
    QLayout
)

from ...signals.types import fSignalVar
from ...common.declarative import fDeclarative


class qMainWindow(fDeclarative,
                  QMainWindow):
    def __init__(
        self, 
        uid: str = None,
        signals:  fSignalVar = None,
        tool_bar: QToolBar = None,
        status_bar: QStatusBar = None,
        dock_widget: QDockWidget = None,
        *args,
        **kwargs
    ):
        QMainWindow.__init__(self)
        fDeclarative.__init__(self, uid, signals, *args, **kwargs)

        self._set_tool_bar(tool_bar)
        self._set_status_bar(status_bar)
        self._set_dock_widget(dock_widget)

        self.__build()

    def __build(self) -> None:
        self.child = self.build()
        if self.child is not None:
            if isinstance(self.child, QLayout):
                self.centralwidget = QWidget(self)
                self.centralwidget.setObjectName("centralwidget")

                self.child.setProperty("parent", self.centralwidget)
                self.centralwidget.setLayout(self.child)

                self.setCentralWidget(self.centralwidget)

            elif isinstance(self.child, QWidget):
                # self.centralwidget = QWidget(self)
                # self.centralwidget.setObjectName("centralwidget")
                # self.child.setParent(self.centralwidget)
                # self.setCentralWidget(self.centralwidget)

                self.child.setParent(self)
                self.setCentralWidget(self.child)
            else:
                raise ValueError(f"build method return type must be instance \
                    of QMainWindow, not '{self.child.__class__}'")

    def _set_tool_bar(self, tool_bar: QToolBar) -> None:
        if tool_bar is not None:
            return self.addToolBar(tool_bar)

    def _set_status_bar(self, status_bar: QStatusBar) -> None:
        if status_bar is not None:
            return self.setStatusBar(status_bar)

    def _set_dock_widget(self, dock_widget: QDockWidget) -> None:
        if dock_widget is not None:
            self.addDockWidget(dock_widget)


class fMainWindow(qMainWindow):
    def __init__(self, 
                 uid: str = None, 
                 signals: fSignalVar = None,
                 home: QWidget = None,
                 tool_bar: QToolBar = None, 
                 status_bar: QStatusBar = None, 
                 dock_widget: QDockWidget = None, 
                 *args, 
                 **kwargs):
        self.home = home
        qMainWindow.__init__(self,
                             uid, 
                             signals, 
                             tool_bar, 
                             status_bar, 
                             dock_widget, 
                             *args, 
                             **kwargs)
    def build(self):
        return self.home