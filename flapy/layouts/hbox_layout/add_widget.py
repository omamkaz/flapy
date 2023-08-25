from ..vbox_layout.add_widget import fVBoxAddWidget
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class fHBoxAddWidget(fVBoxAddWidget):
    def __init__(self, 
                 child: QWidget, 
                 stretch: int = None,
                 alignment: Qt.AlignmentFlag = None) -> None:
        super().__init__(child, stretch, alignment)