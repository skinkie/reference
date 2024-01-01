from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VersionStatusEnumeration(Enum):
    DRAFT = "draft"
    PROPOSED = "proposed"
    VERSIONED = "versioned"
    DEPRECATED = "deprecated"
    OTHER = "other"
