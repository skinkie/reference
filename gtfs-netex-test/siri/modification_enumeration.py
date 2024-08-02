from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class ModificationEnumeration(Enum):
    NEW = "new"
    DELETE = "delete"
    REVISE = "revise"
