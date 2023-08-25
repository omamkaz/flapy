

class ColorCard(qWidget):
    def __init__(self, 
                 color: str, 
                 uid: str = None, 
                 signals: fSignalVar = None, 
                 *args, **kwargs):

        qWidget.__init__(self, uid, signals, *args, **kwargs)

        f = QFrame(self)
        f.setStyleSheet(f"background-color: {color}; border: 1px solid #fff; border-radius: 8px")

# or this way

class ColorCard(qWidget):
    def __init__(self, 
                 color: str, 
                 uid: str = None, 
                 signals: fSignalVar = None, 
                 *args, **kwargs):

        self.color = color

        qWidget.__init__(self, uid, signals, *args, **kwargs)

    def build(self) -> QWidget:
        self.frame = QFrame(self)
        self.frame.setStyleSheet(f"background-color: {self.color}; border: 2px solid #fff; border-radius: 8px")
        return self.frame