from PySide6.QtWidgets import QFormLayout, QWidget, QLayout
from typing import List, Optional, Union, TypeAlias
from ..grid_layout import fGridAddWidget, fGridAddLayout

qFormChildren: TypeAlias = 

class qFormLayout(QFormLayout):
    def __init__(self, 
                 children: List[Union[fGBoxAddLayout, fGBoxAddWidget, QWidget]],
                 id: Optional[str] = None):
        super().__init__()

        self._set_id(id)
        self._set_children(children)

    def _set_id(self, id: str) -> None:
        if id is not None:
            self.setObjectName(id)

    def _set_children(self, 
                      children: List[Union[GBoxAddLayout, GBoxAddWidget, QWidget]]) -> None:

        if not children:
            raise ValueError("children argument should be a list of GBoxAdd class.")

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayout):
                self.addLayout(child)
            
            elif isinstance(child, GBoxAddWidget):
                self.addWidget(*child._build())

            elif isinstance(child, GBoxAddLayout):
                self.addLayout(*child._build())

            else:
                # raise ValueError()
                ...