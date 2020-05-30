from typing import ClassVar

import attr


@attr.s(auto_attribs=True)
class AppConfig:
    ITEM_CHECK: ClassVar[str] = "sampleConfigItem"
    _item_check: bool = True

    @property
    def item_checked(self):
        return self._item_check

    @item_checked.setter
    def item_checked(self, val):
        self._item_check = val
