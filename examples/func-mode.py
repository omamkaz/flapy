import flapy_path

from flapy.signals import fSignalVar, fSignalType
from flapy.widgets import fMainWindow, qWidget, qPushButton
from flapy.layouts import qGridLayout,fGridAddWidget
from flapy import fApi

from PySide6.QtWidgets import QPushButton, QFrame
from PySide6.QtGui import QIcon

import flapy
import random
import sys

colors = ["orange", "blue", "purple", "gray"]
app = flapy.init(sys.argv)


def icon_push_button(icon: str = None) -> QPushButton:
    btn = qPushButton(Disabled=True)
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
                                 border-radius: 8px;""")
def change_value(parent):
    fApi(parent).get("c2").set_color(random.choice(colors))

window = fMainWindow(
    home=qGridLayout(
        children=[
            fGridAddWidget(
                child=ColorCard(color="red",
                                signals=[(fSignalType.mouseClick,
                                            lambda: change_value(window))]),
                row=0,
                column=1
            ),
            fGridAddWidget(
                child=ColorCard(color="blue", 
                                uid="c2"),
                row=1,
                column=1
            ),
            fGridAddWidget(
                child=ColorCard(color="green"),
                row=1,
                column=2,
            ),
            qPushButton(
                icon=QIcon.fromTheme("firefox"),
                text="Click me",
                signals=[(fSignalType.clicked, lambda: print("hi"))]
            )
        ]
    )
)



if __name__ == "__main__":
    window.setWindowTitle("Color Changer")
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec())