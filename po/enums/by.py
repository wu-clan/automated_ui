#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from po.enums import StrEnum


class ByType(StrEnum):
    ID = "id"
    NAME = "name"
    CLASS_NAME = "class"
    TAG_NAME = "tag"
    LINK_TEXT = "link"
    PARTIAL_LINK_TEXT = "plink"
    CSS_SELECTOR = "css"
    XPATH = "xpath"
