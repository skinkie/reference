from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransmissionEnumeration(Enum):
    """Allowed values for Vehicle Transmission.

    +v1.2.2
    """
    AUTOMATIC = "automatic"
    AUTOMATIC4_WHEEL_DRIVE = "automatic4WheelDrive"
    MANUAL = "manual"
    MANUAL4_WHEEL_DRIVE = "manual4WheelDrive"
