from PySide6.QtWidgets import QLabel
from typing import Tuple, Callable, Any, List
from ...common.base import fBase
from ...signals import fSignalType


class qLabel(fBase, QLabel):
    def __init__(self, 
                 uid: str = None,
                 signals: List[Tuple[fSignalType, Callable[..., Any]]] = None,
                 text: str = None,
                 *args,
                 **kwargs):

        QLabel.__init__(self)
        fBase.__init__(self, uid, signals, *args, **kwargs)

        self._set_text(text)

    def _set_text(self, text: str):
        if text is not None:
            self.setText(text)