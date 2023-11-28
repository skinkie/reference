from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContainmentEnumeration(Enum):
    """
    Classification of containment.

    :cvar INLINE: This is a definition of a new entity.
    :cvar BY_REFERENCE: This is a deletion of an existing entity.
    :cvar BY_VERSIONED_REFERENCE:
    :cvar BOTH:
    """
    INLINE = "inline"
    BY_REFERENCE = "byReference"
    BY_VERSIONED_REFERENCE = "byVersionedReference"
    BOTH = "both"
