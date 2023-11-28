from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ClassRefTypeEnumeration(Enum):
    """
    Allowed values for nature of reference.

    :cvar MEMBERS: Include elements that meet selection criteria (e.g.
        validity condition).
    :cvar MEMBER_REFERENCES: Include elements that are referenced by
        primary element. E.g. TYPES OF VALUE, OPERATOR etc.
    :cvar ALL: Include all elements.
    """
    MEMBERS = "members"
    MEMBER_REFERENCES = "memberReferences"
    ALL = "all"
