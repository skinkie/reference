from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DataRoleTypeEnumeration(Enum):
    ALL = "all"
    CREATES = "creates"
    AUGMENTS = "augments"
    VALIDATES = "validates"
    COLLECTS = "collects"
    AGGREGATES = "aggregates"
    DISTRIBUTES = "distributes"
    SECURES = "secures"
    REDISTRIBUTES = "redistributes"
    SUPPORTS = "supports"
    OWNS = "owns"
    OTHER = "other"
