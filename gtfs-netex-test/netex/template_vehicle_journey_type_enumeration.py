from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TemplateVehicleJourneyTypeEnumeration(Enum):
    """
    Allowed values for TEMPLATE VEHICLE JOURNEY type.

    :cvar HEADWAY: INTERCHANGE is considered a possible connection
        between journeys.
    :cvar RHYTHMIC: INTERCHANGE is advertised to public as a possible
        connection between journeys.
    :cvar OTHER:
    """
    HEADWAY = "headway"
    RHYTHMIC = "rhythmic"
    OTHER = "other"
