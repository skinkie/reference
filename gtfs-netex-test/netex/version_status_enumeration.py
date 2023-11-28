from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VersionStatusEnumeration(Enum):
    """
    Allowed values for Statuses of VERSION.
    """
    DRAFT = "draft"
    PROPOSED = "proposed"
    VERSIONED = "versioned"
    DEPRECATED = "deprecated"
    OTHER = "other"
