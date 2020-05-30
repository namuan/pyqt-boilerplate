import logging


class MainWindowController:
    def __init__(self, parent_window, app):
        self.parent = parent_window
        self.initial_load = True
        self.app = app
        self.init_app()

    def init_app(self):
        self.app.init()
        self.app.init_logger()
        if self.app.geometry():
            self.parent.restoreGeometry(self.app.geometry())
        if self.app.window_state():
            self.parent.restoreState(self.app.window_state())

    def save_settings(self):
        self.app.save_window_state(
            geometry=self.parent.saveGeometry(), window_state=self.parent.saveState()
        )
        logging.info("Saved settings for Main Window")

    def shutdown(self):
        self.save_settings()

    def after_window_loaded(self):
        if not self.initial_load:
            return

        self.initial_load = False
        self.on_first_load()

    def on_first_load(self):
        self.parent.scratch_pad_controller.init()
