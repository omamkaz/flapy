from enum import Enum
from PySide6.QtWidgets import (
    QLabel, 
    QPushButton, 
    QWidget,
    QLineEdit,
    QScrollArea,
    QBoxLayout,
    QFormLayout,
    QHBoxLayout,
    QGridLayout,
    QVBoxLayout,
)
from PySide6.QtCore import QObject


class fWidgetType(Enum):
    # Widgets
    any = QObject
    label = QLabel
    widget = QWidget
    line_edit = QLineEdit
    push_button = QPushButton
    scroll_area = QScrollArea

    # Layouts
    box_layout = QBoxLayout
    form_layout = QFormLayout
    hbox_layout = QHBoxLayout
    grid_layout = QGridLayout
    vbox_layout = QVBoxLayout