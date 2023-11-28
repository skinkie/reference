from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeadRunTypeEnumeration(Enum):
    """Allowed values for DEAD RUN.

    type.

    :cvar GARAGE_RUN_OUT: INTERCHANGE is considered a possible
        connection between journeys.
    :cvar GARAGE_RUN_IN: INTERCHANGE is advertised to public as a
        possible connection between journeys.
    :cvar TURNING_MANOEUVRE: INTERCHANGE is actively managed as a
        possible connection between journeys and passengers are informed
        of real-time alterations.
    :cvar OTHER:
    """
    GARAGE_RUN_OUT = "garageRunOut"
    GARAGE_RUN_IN = "garageRunIn"
    TURNING_MANOEUVRE = "turningManoeuvre"
    OTHER = "other"
