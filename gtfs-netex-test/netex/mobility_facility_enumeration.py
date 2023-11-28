from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MobilityFacilityEnumeration(Enum):
    """Allowed values for Mobility Facility: TPEG pti_table 23.

    :cvar UNKNOWN: pti255_4
    :cvar LOW_FLOOR: pti23_16_1
    :cvar STEP_FREE_ACCESS: pti23_16_3
    :cvar SUITABLE_FOR_WHEELCHAIRS: pti23_16_1
    :cvar SUITABLE_FOR_HEAVILIY_DISABLED:
    :cvar BOARDING_ASSISTANCE: pti23_16_2
    :cvar ONBOARD_ASSISTANCE:
    :cvar UNACCOMPANIED_MINOR_ASSISTANCE:
    :cvar TACTILE_PLATFORM_EDGES:
    :cvar TACTILE_GUIDING_STRIPS:
    """
    UNKNOWN = "unknown"
    LOW_FLOOR = "lowFloor"
    STEP_FREE_ACCESS = "stepFreeAccess"
    SUITABLE_FOR_WHEELCHAIRS = "suitableForWheelchairs"
    SUITABLE_FOR_HEAVILIY_DISABLED = "suitableForHeaviliyDisabled"
    BOARDING_ASSISTANCE = "boardingAssistance"
    ONBOARD_ASSISTANCE = "onboardAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    TACTILE_PLATFORM_EDGES = "tactilePlatformEdges"
    TACTILE_GUIDING_STRIPS = "tactileGuidingStrips"
