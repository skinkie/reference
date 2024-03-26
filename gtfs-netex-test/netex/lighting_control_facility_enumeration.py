from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LightingControlFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    NONE = "none"
    TINTED_WINDOWS = "tintedWindows"
    BLINDS = "blinds"
    CURTAINS = "curtains"
    DIMMABLE_LIGHTS = "dimmableLights"
    LIGHTS_ALWAYS_ON = "lightsAlwaysOn"
    NO_NATURAL_LIGHT = "noNaturalLight"
    OTHER = "other"
