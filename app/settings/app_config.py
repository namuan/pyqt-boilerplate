from typing import ClassVar

import attr


@attr.s(auto_attribs=True)
class AppConfig:
    NOTES_FILE_KEY: ClassVar[str] = "notesFile"
    _notes_file: str = ""

    @property
    def notes_file(self):
        return self._notes_file

    @notes_file.setter
    def notes_file(self, val):
        self._notes_file = val
