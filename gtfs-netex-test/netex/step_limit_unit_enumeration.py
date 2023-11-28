from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StepLimitUnitEnumeration(Enum):
    """
    Allowed values for STEP LIMIT UNIT Type.
    """
    STOPS = "stops"
    STOPS_INCLUDING_PASS_THROUGH_STOPS = "stopsIncludingPassThroughStops"
    SECTIONS = "sections"
    ZONES = "zones"
    NETWORKS = "networks"
    OPERATORS = "operators"
    COUNTRIES = "countries"
