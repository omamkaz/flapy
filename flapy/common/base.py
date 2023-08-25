from PySide6.QtCore import Slot, Qt, QEvent, QObject
from PySide6.QtGui import QEnterEvent, QMouseEvent
from ..signals import fSignalType, fSignals, fSignalVar
from .widget_type import fWidgetType


class fBase:
    """
    this class is abstract for any widget.
    """
    def __init__(self, 
                 uid: str = None,
                 signals: fSignalVar = None,
                 *args,
                 **kwargs):

        self.fsignals = fSignals(self)

        self.setMouseTracking(True)
        self.setTabletTracking(True)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, True)

        self._set_uid(uid)
        self._set_signals(signals)

    @Slot()
    def enterEvent(self, event: QEnterEvent) -> None:
        self.fsignals.mouse_hover.emit()
        return super().enterEvent(event)

    @Slot()
    def leaveEvent(self, event: QEvent) -> None:
        self.fsignals.mouse_leave.emit()
        return super().leaveEvent(event)

    @Slot()
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.fsignals.mouse_double_click.emit()
        return super().mouseDoubleClickEvent(event)

    @Slot()
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.fsignals.mouse_click.emit()
        return super().mousePressEvent(event)

    def _set_uid(self, uid: str):
        if uid is not None:
            self.setObjectName(uid.strip())

    def _set_signals(self, signals: fSignalVar):
        if not signals:
            return
        
        _members = [mn.lower() for mn in fSignalType._member_names_]
        for s in signals:
            try:
                sname = (s[0].name if isinstance(s[0], fSignalType) else s[0]).lower()
                if sname in _members:
                    if (slot := self.fsignals.__getattribute__(sname)) is not None:
                        slot.connect(s[1])
            except TypeError as err:
                print(err)
                pass

    def _get_wtype(self, w_type: fWidgetType = fWidgetType.any):
        return (w_type.value
                if isinstance(w_type, fWidgetType) 
                else w_type)

    def get(self, 
            uid: str, 
            w_type: fWidgetType = fWidgetType.any) -> QObject:
        return self.findChild(self._get_wtype(w_type), 
                              uid.strip(), 
                              Qt.FindChildOption.FindChildrenRecursively)