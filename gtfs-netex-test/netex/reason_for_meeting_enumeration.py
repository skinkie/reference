from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReasonForMeetingEnumeration(Enum):
    """
    Allowed values for REASON FOR JOURNEY MEETING.

    :cvar SERVICE_FACILITY: INTERCHANGE is considered a possible
        connection between journeys.
    :cvar JOINING: INTERCHANGE is advertised to public as a possible
        connection between journeys.
    :cvar TARIFF_SECTION: INTERCHANGE is actively managed as a possible
        connection between journeys and passengers are informed of real-
        time alterations.
    :cvar SPLITTING:
    """
    SERVICE_FACILITY = "serviceFacility"
    JOINING = "joining"
    TARIFF_SECTION = "tariffSection"
    SPLITTING = "splitting"
