from PySide6.QtWidgets import QWidget, QLayout
from ...signals.types import fSignalVar
from ...common.declarative import fDeclarative


class _qWidget(fDeclarative, QWidget):
    def __init__(self, 
                 uid: str = None,
                 signals: fSignalVar = None,
                 *args,
                 **kwargs):
        QWidget.__init__(self)
        fDeclarative.__init__(self, uid, signals, *args, **kwargs)


class qWidget(_qWidget):
    def __init__(self, 
                 uid: str = None,
                 signals: fSignalVar = None,
                 *args,
                 **kwargs):
        _qWidget.__init__(self, uid, signals, *args, **kwargs)

        self.__build()

    def build(self):
        return None

    def __build(self):
        self.child = self.build()
        if self.child is not None:
            if isinstance(self.child, QWidget):
                self.child.setParent(self)
            elif isinstance(self.child, QLayout):
                self.child.setProperty("parent", self)
                self.setLayout(self.child)
            else:
                raise ValueError(f"build method return type must be instance \
                    of QWidget OR QLayout, not '{self.child.__class__}'")


class fWidget(qWidget):
    def __init__(self, 
                 uid: str = None, 
                 child: QWidget = None,
                 signals: fSignalVar = None, 
                 *args, 
                 **kwargs):
        self.child = child
        super().__init__(uid, signals, *args, **kwargs)

    def build(self):
        return self.child