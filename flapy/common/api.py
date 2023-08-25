from PySide6.QtCore import Qt, QObject
from .widget_type import fWidgetType


class fApi:
    def __init__(self, 
                 parent: QObject, 
                 w_type: fWidgetType = fWidgetType.any):

        self.parent = parent
        self.w_type = w_type

    def _get_wtype(self, w_type: fWidgetType = fWidgetType.any):
        return (w_type.value 
                if isinstance(w_type, fWidgetType) 
                else w_type)

    def get(self, uid: str, w_type: fWidgetType = fWidgetType.any) -> QObject:
        return self.parent.findChild(self._get_wtype(w_type 
                                                     if w_type is not None 
                                                     else self.w_type),
                                     uid.strip(),
                                     Qt.FindChildOption.FindChildrenRecursively)