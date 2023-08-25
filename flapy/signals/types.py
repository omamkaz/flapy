from enum import Enum, auto
from typing import List, Tuple, Callable, Any, TypeAlias


class fSignalType(Enum):
    """ 
    Enumerates Qt signal names so that all signals are in one easily-accessible place. It is
    still up to initializer functions to implement these signals in a consistent manner.
    """

    # Bult-in methods
    CLICKED = auto()
    PRESSED = auto()
    RELEASED = auto()
    TEXT_CHANGED = auto()

    # External methods
    MOUSE_CLICK = auto()
    MOUSE_DOUBLE_CLICK = auto()
    MOUSE_HOVER = auto()
    MOUSE_LEAVE = auto()

fSignalVar: TypeAlias = List[Tuple[fSignalType, Callable[..., Any]]]