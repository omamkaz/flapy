from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class GridAddWidget:
    def __init__(
        self,
        child: QWidget,
        row: int = None,
        column: int = None,
        rowSpan: int = None,
        columnSpan: int = None,
        alignment: Qt.AlignmentFlag = None
    ) -> None:

        self.child = child
        self.row = row
        self.column = column
        self.rowSpan = rowSpan
        self.columnSpan = columnSpan
        self.alignment = alignment

    def _build(self):
        if not self.child:
            raise AttributeError("child should be QWidget or QLayout")

        for attr in filter(lambda x: not x.startswith("_"), dir(self)):
            if (result := getattr(self, attr)) is not None:
                yield result
