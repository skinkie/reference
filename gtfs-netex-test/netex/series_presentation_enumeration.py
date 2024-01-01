from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesPresentationEnumeration(Enum):
    NONE = "none"
    REQUIRED = "required"
    OPTIONAL_LEFT = "optionalLeft"
    OPTIONAL_RIGHT = "optionalRight"
