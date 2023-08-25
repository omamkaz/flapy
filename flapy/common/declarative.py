from .base import fBase
from ..signals import fSignalVar


class fDeclarative(fBase):
    def __init__(self,
                 uid: str = None,
                 signals: fSignalVar = None,
                 *args,
                 **kwargs) -> None:
        fBase.__init__(self, uid, signals, *args, **kwargs)

    def build(self) -> object:
        raise NotImplementedError()

    def rebuild(self) -> None:
        raise NotImplementedError()