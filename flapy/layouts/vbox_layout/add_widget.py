from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class fVBoxAddWidget:
    def __init__(self, 
                 child: QWidget, 
                 stretch: int = None,
                 alignment: Qt.AlignmentFlag = None) -> None:

        self.child = child
        self.stretch = stretch
        self.alignment = alignment

    def _build(self):
        if not self.child:
            raise AttributeError("child should be QWidget | QLayout")

        for attr in (
            self.child,
            self.stretch,
            self.alignment
        ):
            if attr is not None:
                yield attr