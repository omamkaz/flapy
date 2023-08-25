from enum import Enum, auto
from typing import List, Tuple, Callable, Any, TypeAlias


class fSignalType(Enum):
    """ 
    Enumerates Qt signal names so that all signals are in one easily-accessible place. 
    It is still up to initializer functions to implement these signals in a consistent manner.
    """

    ## Bult-in methods
    # QPushButton
    clicked = auto()
    pressed = auto()
    released = auto()
    
    # QLineEdit
    textChanged = auto()
    textEdited = auto()
    editingFinished = auto()
    returnPressed = auto()

    # QSlider
    valueChanged = auto()
    sliderMoved = auto()
    sliderPressed = auto()

    # QMainWindow
    windowTitleChanged = auto()

    # Additional methods
    mouseClick = auto()
    mouseDoubleClick = auto()
    mouseHover = auto()
    mouseLeave = auto()


fSignalVar: TypeAlias = List[Tuple[fSignalType, Callable[..., Any]]]