from PyQt5.QtWidgets import QFileDialog

from app.settings.app_config import AppConfig
from app.views.configuration_dialog import ConfigurationDialog


class ConfigController:
    def __init__(self, parent_view, app):
        self.view = ConfigurationDialog(parent_view)
        self.parent_view = parent_view
        self.app = app

        # ui events
        self.view.btn_save_configuration.pressed.connect(self.on_success)
        self.view.btn_cancel_configuration.pressed.connect(self.ignore_changes)
        self.view.btn_select_notes_file.pressed.connect(self.select_notes_file)

    def select_notes_file(self):
        file_location, _ = QFileDialog.getSaveFileName(
            self.parent_view, "Select Notes File", self.app.app_dir.as_posix()
        )
        if file_location:
            self.view.txt_notes_file.setText(file_location)

    def ignore_changes(self):
        self.view.reject()

    def on_success(self):
        app_config = self.form_to_object()
        self.app.save_configuration(app_config)
        self.view.accept()

    def show_dialog(self):
        app_config = self.app.load_configuration()
        self.object_to_form(app_config)
        self.view.show()

    def form_to_object(self):
        config = AppConfig()
        config.notes_file = self.view.txt_notes_file.text()
        return config

    def object_to_form(self, app_config: AppConfig):
        self.view.txt_notes_file.setText(app_config.notes_file)
