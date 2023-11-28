from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StatusEnumeration(Enum):
    """Indicates whether the ENTITY this annotates is available for use.

    Use of this attribute allows entities to be retired without deleting
    the details from the dataset.

    :cvar ACTIVE: Entity is active.
    :cvar INACTIVE: Entity is inactive.
    :cvar OTHER: Entity is still active but is in the process of being
        made inactive.
    """
    ACTIVE = "active"
    INACTIVE = "inactive"
    OTHER = "other"
