
## it's work!, but still you can't use default methods like signals, uid, ...etc your need to create them
class IconPushButton(QPushButton):
    def __init__(self, icon: str = None):
        super().__init__()

        self.setIcon(QIcon.fromTheme(icon))

# in this way you just want to work with pushButton direct
class IconPushButton(fDeclarative, QPushButton):
    def __init__(self, 
                 icon: str = None,
                 uid: str = None, 
                 signals: fSignalVar = None, 
                 *args, **kwargs) -> None:
        QPushButton.__init__(self)
        fDeclarative.__init__(self, uid, signals, *args, **kwargs)

        self.setIcon(QIcon.fromTheme(icon))

# in this way will create push button inside the QWidget as container, this way is recommended by default to custom padding, margin, ...etc
class IconPushButton(qWidget):
    def __init__(self, 
                 icon: str = None, 
                 uid: str = None, 
                 signals: fSignalVar = None, 
                 *args, **kwargs):
        
        qWidget.__init__(self, uid, signals, *args, **kwargs)

        btn = QPushButton(self)
        btn.setIcon(QIcon.fromTheme(icon))

# yes you can, just create some function and call it
def icon_push_button(icon: str = None) -> QPushButton:
    btn = QPushButton()
    btn.setIcon(QIcon.fromTheme(icon))
    return btn