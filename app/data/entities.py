import json

import attr
import cattr

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppState:
    record_type: str = APP_STATE_RECORD_TYPE
    scratch_note: str = ""

    @classmethod
    def from_json_str(cls, json_str):
        json_obj = json.loads(json_str)
        return cls.from_json(json_obj)

    @classmethod
    def from_json(cls, json_obj):
        if not json_obj:
            return cls()
        return cattr.structure(json_obj, cls)

    def to_json(self):
        return cattr.unstructure(self)

    def to_json_str(self):
        return json.dumps(self.to_json())
