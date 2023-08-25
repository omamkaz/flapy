from PySide6.QtWidgets import QGridLayout, QWidget, QLayout
from typing import List, Optional, Union, TypeAlias
from .add_widget import fGridAddWidget
from .add_layout import fGridAddLayout


qGridChildren: TypeAlias = List[Union[fGridAddLayout, fGridAddWidget, QWidget, QLayout]]

class qGridLayout(QGridLayout):
    def __init__(self, 
                 uid: Optional[str] = None,
                 children: qGridChildren = None):
        super().__init__()

        self._set_uid(uid)
        self._set_children(children)

    def _set_uid(self, uid: str) -> None:
        if uid is not None:
            self.setObjectNameu(uid.strip())

    def _set_children(self, children: qGridChildren) -> None:
        if not children:
            raise ValueError("children argument should be a list of qGridChildren typeVar.")

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayout):
                self.addLayout(child)
            
            elif isinstance(child, fGridAddWidget):
                self.addWidget(*child._build())

            elif isinstance(child, fGridAddLayout):
                self.addLayout(*child._build())