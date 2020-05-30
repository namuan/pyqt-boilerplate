from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QEvent


class ScratchPadEvents(QObject):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.FocusOut:
            self.save_scratch_pad()

        return super().eventFilter(source, event)

    def save_scratch_pad(self):
        scratch = self.parent.txt_scratch_pad.toPlainText()
        self.app.data.update_scratch_note(scratch)


class ScratchPadController:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.events = ScratchPadEvents(self.parent, self.app)

        # installing event filter
        self.parent.txt_scratch_pad.installEventFilter(self.events)

    def init(self):
        scratch_note = self.app.data.get_scratch_note()
        self.parent.txt_scratch_pad.setPlainText(scratch_note)

    def save_scratch_pad(self):
        self.events.save_scratch_pad()
