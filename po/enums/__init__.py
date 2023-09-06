#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum


class EnumBase(Enum):
    @classmethod
    def get_member_keys(cls) -> list[str]:
        return [name for name in cls.__members__.keys()]

    @classmethod
    def get_member_values(cls) -> list:
        return [item.value for item in cls.__members__.values()]


class IntEnum(int, EnumBase):
    """整型枚举"""

    pass


class StrEnum(str, EnumBase):
    """字符串枚举"""

    pass
