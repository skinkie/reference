from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DataRoleTypeEnumeration(Enum):
    """
    Allowed values for Administrative Roles.
    """
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
