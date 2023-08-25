from ..vbox_layout.add_layout import fVBoxAddLayout
from PySide6.QtWidgets import QLayout


class fBoxAddLayout(fVBoxAddLayout):
    def __init__(self, 
                 child: QLayout, 
                 stretch: int = None) -> None:
        super().__init__(child, stretch)