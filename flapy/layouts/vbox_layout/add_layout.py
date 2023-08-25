from PySide6.QtWidgets import QLayout


class fVBoxAddLayout:
    def __init__(self, 
                 child: QLayout, 
                 stretch: int = None) -> None:

        self.child = child
        self.stretch = stretch

    def _build(self):
        if not self.child:
            raise AttributeError("child should be QWidget | QLayout")

        for attr in (
            self.child,
            self.stretch
        ):
            if attr is not None:
                yield attr
