from PySide6.QtWidgets import QHBoxLayout, QWidget, QLayout
from typing import List, Union, TypeAlias
from .add_widget import fHBoxAddWidget
from .add_layout import fHBoxAddLayout


qHBoxChildren: TypeAlias = List[Union[fHBoxAddLayout, fHBoxAddWidget, QWidget, QLayout]]

class qHBoxLayout(QHBoxLayout):
    def __init__(self, 
                 uid: str = None,
                 children: qHBoxChildren = None):
        super().__init__()

        self._set_uid(uid)
        self._set_children(children)
    
    def _set_uid(self, uid: str) -> None:
        if uid is not None:
            self.setObjectName(uid)

    def _set_children(self, children: qHBoxChildren) -> None:
        if not children:
            raise ValueError("children argument should be a list of qHBoxChildren typeVar.")

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayout):
                self.addLayout(child)
            
            elif isinstance(child, fHBoxAddWidget):
                self.addWidget(*child._build())

            elif isinstance(child, fHBoxAddLayout):
                self.addLayout(*child._build())

            else:
                # raise ValueError()
                ...