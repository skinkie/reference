from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MandatoryEnumeration(Enum):
    """
    Allowed values for Mandatory.

    :cvar REQUIRED: Include elements that meet selection criteria (e.g.
        validity condition).
    :cvar OPTIONAL: Include elements that are referenced by primary
        element. E.g. TYPES OF VALUE, OPERATOR etc.
    :cvar NOT_ALLOWED: Include all elements.
    """
    REQUIRED = "required"
    OPTIONAL = "optional"
    NOT_ALLOWED = "notAllowed"
