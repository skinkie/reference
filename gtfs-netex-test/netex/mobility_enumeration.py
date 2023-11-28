from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MobilityEnumeration(Enum):
    """
    Allowed values for of mobility needs.
    """
    WHEELCHAIR = "wheelchair"
    ASSISTED_WHEELCHAIR = "assistedWheelchair"
    MOTORIZED_WHEELCHAIR = "motorizedWheelchair"
    MOBILITY_SCOOTER = "mobilityScooter"
    ROAD_MOBILITY_SCOOTER = "roadMobilityScooter"
    WALKING_FRAME = "walkingFrame"
    RESTRICTED_MOBILITY = "restrictedMobility"
    OTHER_MOBILITY_NEED = "otherMobilityNeed"
    NORMAL = "normal"
