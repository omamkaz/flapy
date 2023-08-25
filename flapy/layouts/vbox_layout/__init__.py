from PySide6.QtWidgets import QVBoxLayout, QWidget, QLayout
from typing import List, Union, TypeAlias
from .add_widget import fVBoxAddWidget
from .add_layout import fVBoxAddLayout


qVBoxChildren: TypeAlias = List[Union[fVBoxAddLayout, fVBoxAddWidget, QWidget, QLayout]]


class qVBoxLayout(QVBoxLayout):
    def __init__(self,
                 uid: str = None,
                 children: qVBoxChildren = None):
        super().__init__()

        self._set_uid(uid)
        self._set_children(children)
    
    def _set_id(self, uid: str) -> None:
        if uid is not None:
            self.setObjectName(uid)

    def _set_children(self, children: qVBoxChildren) -> None:
        if not children:
            raise ValueError("children argument should be a list of qVBoxChildren typeVar.")

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayout):
                self.addLayout(child)
            
            elif isinstance(child, fVBoxAddWidget):
                self.addWidget(*child._build())

            elif isinstance(child, fVBoxAddLayout):
                self.addLayout(*child._build())

            else:
                # raise ValueError()
                ...