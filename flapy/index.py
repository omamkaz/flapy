from .widgets.app import fApp
from typing import Sequence


def init(arg: Sequence[str] = None):
    return fApp(arg)
