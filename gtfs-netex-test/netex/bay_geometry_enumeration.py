from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BayGeometryEnumeration(Enum):
    UNSPECIFIED = "unspecified"
    ORTHOGONAL = "orthogonal"
    ANGLED = "angled"
    PARALLEL = "parallel"
    FREE_FORMAT = "freeFormat"
    OTHER = "other"
