from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleAccessFacilityEnumeration(Enum):
    """Allowed values for Vehicle Access Facility.

    NB. These are the  properties of access to a VEHICLE. +1.1
    """
    UNKNOWN = "unknown"
    WHEELCHAIR_LIFT = "wheelchairLift"
    MANUAL_RAMP = "manualRamp"
    AUTOMATIC_RAMP = "automaticRamp"
    STEPS = "steps"
    SLIDING_STEP = "slidingStep"
    NARROW_ENTRANCE = "narrowEntrance"
    VALIDATOR = "validator"
