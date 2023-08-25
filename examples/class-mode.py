from flapy.signals import fSignalVar, fSignalType
from flapy.widgets import fApp, qMainWindow, qWidget
from flapy.layouts import qGridLayout, fGridAddWidget
from flapy import fApi

from PySide6.QtWidgets import QDockWidget, QPushButton, QFrame, QStatusBar, QToolBar
from PySide6.QtGui import QIcon
import random


def icon_push_button(icon: str = None) -> QPushButton:
    btn = QPushButton()
    btn.setIcon(QIcon.fromTheme(icon))
    return btn


class ColorCard(qWidget):
    def __init__(self, 
                 color: str, 
                 uid: str = None, 
                 signals: fSignalVar = None, 
                 *args, **kwargs):

        self.color = color

        qWidget.__init__(self, uid, signals, *args, **kwargs)

        self.frame = QFrame(self)
        self.set_color(color)

    def set_color(self, color: str) -> None:
        self.color = color
        self.frame.setStyleSheet(f"""
                                 background-color: {color}; 
                                 border: 1px solid #fff; 
                                 border-radius: 8px""")


class Window(qMainWindow):
    def __init__(self, 
                 uid: str = None, 
                 signals: fSignalVar = None, 
                 tool_bar: QToolBar = None, 
                 status_bar: QStatusBar = None, 
                 dock_widget: QDockWidget = None, 
                 *args, 
                 **kwargs):
        super().__init__(uid, 
                         signals, 
                         tool_bar, 
                         status_bar, 
                         dock_widget, 
                         *args, 
                         **kwargs)

        self.colors = ["orange", "blue", "purple", "gray"]

    def change_value(self):
        fApi(self).get("c2").set_color(random.choice(self.colors))

    def build(self) -> object:
        self.value = "blue"

        return qGridLayout(
            children=[
                fGridAddWidget(
                    child=ColorCard(color="red",
                                    signals=[(fSignalType.MOUSE_CLICK, 
                                              self.change_value)]),
                    row=0,
                    column=1
                ),
                fGridAddWidget(
                    child=ColorCard(color=self.value, 
                                    uid="c2"),
                    row=1,
                    column=1
                ),
                fGridAddWidget(
                    child=ColorCard(color="green"),
                    row=1,
                    column=2,
                ),
                icon_push_button(icon="firefox"),
            ]
        )


def main():
    import sys
    app = fApp(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()