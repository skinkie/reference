from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PublicityChannelEnumeration(Enum):
    """
    Allowed values for Publicity Channel.

    :cvar ALL: INTERCHANGE is considered a possible connection between
        journeys.
    :cvar PRINTED_MEDIA: INTERCHANGE is advertised to public as a
        possible connection between journeys.
    :cvar DYNAMIC_MEDIA: INTERCHANGE is actively managed as a possible
        connection between journeys and passengers are informed of real-
        time alterations.
    :cvar NONE:
    """
    ALL = "all"
    PRINTED_MEDIA = "printedMedia"
    DYNAMIC_MEDIA = "dynamicMedia"
    NONE = "none"
