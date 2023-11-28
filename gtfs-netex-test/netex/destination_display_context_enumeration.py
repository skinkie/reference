from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DestinationDisplayContextEnumeration(Enum):
    """Allowed values forr Destination Display Context.

    +v1.1.
    """
    ANY = "any"
    CONTINUE_TO = "continueTo"
    ENDS_AT = "endsAt"
    TRANSFER_AT = "transferAt"
    VIA = "via"
    IN_MESSAGE = "inMessage"
    UNKNOWN = "unknown"
