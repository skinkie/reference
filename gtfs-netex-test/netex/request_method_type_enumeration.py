from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RequestMethodTypeEnumeration(Enum):
    """
    Allowed values for Stop RequestMethod.

    :cvar NONE_REQUIRED: No action required to request stop
    :cvar HAND_SIGNAL: Make hand signal to request stop
    :cvar TURN_ON_LIGHT: Call number to request stop
    :cvar STOP_BUTTON: Press button at stop to request stop
    :cvar PHONE_CALL: Call number to request stop
    :cvar MOBILE_APP: Use mobile Application to request stop
    :cvar SMS: Use Sms to request stop
    :cvar SPEAK_TO_DRIVER_ONBOARD: Tell the driver to request stop.
        Mainly used for on demand traffic, where the route depends on
        where passengers want to leave the vehicle.
    :cvar OTHER: Use other method to request stop
    """
    NONE_REQUIRED = "noneRequired"
    HAND_SIGNAL = "handSignal"
    TURN_ON_LIGHT = "turnOnLight"
    STOP_BUTTON = "stopButton"
    PHONE_CALL = "phoneCall"
    MOBILE_APP = "mobileApp"
    SMS = "sms"
    SPEAK_TO_DRIVER_ONBOARD = "speakToDriverOnboard"
    OTHER = "other"
