from PySide6.QtWidgets import QPushButton
from typing import Tuple, Callable, Any, List
from ...common.base import fBase
from ...signals.types import fSignalType


class qPushButton(fBase, QPushButton):
    def __init__(self, 
                 uid: str = None,
                 signals: List[Tuple[fSignalType, Callable[..., Any]]] = None,
                 text: str = None,
                 *args,
                 **kwargs):
        QPushButton.__init__(self)
        fBase.__init__(self, uid, signals, *args, **kwargs)

        self.setAutoRepeat(kwargs.get('auto_repeat', False))
        self.setAutoRepeatDelay(kwargs.get('repeat_delay', 500))
        self.setAutoRepeatInterval(kwargs.get('repeat_interval', 500))

        self._set_text(text)

        # self._state = 0

    def _set_text(self, text: str):
        if text is not None:
            self.setText(text)

    # def _set_id(self, id: str):
    #     if id is not None:
    #         self.setObjectName(id)

    # def _set_signals(self, signals: list[Tuple[SignalType, Callable[..., Any]]]):
    #     if not signals:
    #         return

    #     for s in signals:
    #         signal = s[0]
    #         slot = s[1]
    #         try:
    #             if signal == SignalType.CLICK:
    #                 self.clicked.connect(slot)
    #         except TypeError:
    #             pass
    
    # def _handleClicked(self):
    #     if self.isDown():
    #         if self._state == 0:
    #             self._state = 1
    #             print ('press')
    #         else:
    #             print ('repeat')
    #     elif self._state == 1:
    #         self._state = 0
    #         print ('release')
    #     else:
    #         print ('click')