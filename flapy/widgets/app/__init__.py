#!/usr/bin/python3

from typing import Sequence, List
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QStyleFactory


class fApp(QApplication):
    on_inactive = Signal()
    on_active = Signal()
    on_hidden = Signal()
    on_suspend = Signal()

    def __init__(self, arg: Sequence[str] = None) -> None:
        if arg is not None:
            super().__init__(arg)
        else:
            super().__init__()

        ## it's default enabled by the developer 
        self.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
        self.setAttribute(Qt.ApplicationAttribute.AA_DontCreateNativeWidgetSiblings, True)

        self.applicationStateChanged.connect(self._applicationStateChanged)

    def _applicationStateChanged(self, event):
        if event == Qt.ApplicationState.ApplicationInactive:
            self.on_inactive.emit()
        elif event == Qt.ApplicationState.ApplicationActive:
            self.on_active.emit()
        elif event == Qt.ApplicationState.ApplicationHidden:
            self.on_hidden.emit()
        elif event == Qt.ApplicationState.ApplicationSuspended:
            self.on_suspend.emit()

    def run(self) -> int:
        return self.exec()

    # theme methods        
    def list_themes(self) -> List[str]:
        return QStyleFactory.keys()

    def current_theme(self) -> str:
        return self.style().name()

    def set_theme(self, name: str):
        name = name.lower().strip()
        if name not in [n.lower() for n in QStyleFactory.keys()]:
            raise ValueError(f"theme '{name}' not found please call list_themes to \
                see all available themes in your system.")

        self.setStyle(QStyleFactory.create(name))
