from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QColor, QRgba64
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from typing import Union, Any, Tuple


class GlobalColor:
    ...


class DropShadow(QGraphicsDropShadowEffect):
    def __init__(self,
                 id: str = None,
                 blur_radius: float = None,
                 color: Union[QColor, QRgba64, Any, GlobalColor, str, int] = None,
                 offset: Union[QPointF, QPoint, Tuple[float, float]] = None):
        super().__init__()

        self._set_id(id)
        self._set_blur_radius(blur_radius)
        self._set_color(color)
        self._set_offset(offset)

    def _set_id(self, id: str):
        if id is not None:
            self.setObjectName(id)

    def _set_blur_radius(self, blur_radius: float):
        if blur_radius is not None:
            self.setBlurRadius(blur_radius)
    
    def _set_color(self, color: Union[QColor, QRgba64, Any, GlobalColor, str, int]):
        if color is not None:
            self.setColor(color)

    def _set_offset(self, offset: Union[QPointF, QPoint, Tuple[float, float], float]):
        if offset is not None:
            if isinstance(offset, tuple | list):
                self.setOffset(*offset)
            else:
                self.setOffset(*[offset])