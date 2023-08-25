from PySide6.QtWidgets import QBoxLayout, QWidget, QLayout
from typing import List, Union, TypeAlias
from .add_layout import fBoxAddLayout
from .add_widget import fBoxAddWidget


qBoxChildren: TypeAlias = List[Union[fBoxAddLayout, fBoxAddWidget, QWidget, QLayout]]

class qBoxLayout(QBoxLayout):
    def __init__(self, 
                 uid: str = None, 
                 children: qBoxChildren = None):
        super().__init__()

        self._set_uid(uid)
        self._set_children(children)

    def _set_uuid(self, uid: str) -> None:
        if uid is not None:
            self.setObjectName(uid)

    def _set_children(self, children: qBoxChildren) -> None:

        if not children:
            raise ValueError("children argument should be a list of qBoxChildren typeVar.")

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)
                
            elif isinstance(child, QLayout):
                self.addLayout(child)
            
            elif isinstance(child, fBoxAddWidget):
                self.addWidget(*child._build())

            elif isinstance(child, fBoxAddLayout):
                self.addLayout(*child._build())

            else:
                # raise ValueError()
                ...