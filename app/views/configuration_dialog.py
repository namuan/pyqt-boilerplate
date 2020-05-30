from PyQt5.QtWidgets import QDialog

from app.generated.ConfigurationDialog_ui import Ui_Configuration


class ConfigurationDialog(QDialog, Ui_Configuration):
    def __init__(self, parent=None):
        super(ConfigurationDialog, self).__init__(parent)
        self.setupUi(self)
