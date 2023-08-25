from PySide6.QtWidgets import QFrame


class Frame(QFrame):
    def __init__(self, 
                 id: str = None,
                 **kwargs):
        super().__init__()

        self._set_id(id)
        self._set_widget(text)

    def _set_text(self, text: str):
        if text is not None:
            self.setText(text)

    def _set_id(self, id: str):
        if id is not None:
            self.setObjectName(id)