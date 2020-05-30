import logging

from pathlib import Path

UTF8_ENCODING = "utf-8"


class DataStore:
    def __init__(self, notes_path):
        self.db = Path(notes_path)
        self.create_if_not_exists()

    def update_store(self, new_notes_file):
        self.db = Path(new_notes_file)
        self.create_if_not_exists()

    def create_if_not_exists(self):
        if not self.db.exists():
            self.db.write_text("", encoding=UTF8_ENCODING)

    def update_scratch_note(self, scratch_note):
        logging.debug("Updating Scratch Pad: {}, Characters: {}".format(self.db, len(scratch_note)))
        if not scratch_note:
            return

        self.db.write_text(scratch_note, encoding=UTF8_ENCODING)

    def get_scratch_note(self):
        return self.db.read_text(encoding=UTF8_ENCODING)
