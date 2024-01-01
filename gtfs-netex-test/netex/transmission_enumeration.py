from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransmissionEnumeration(Enum):
    AUTOMATIC = "automatic"
    AUTOMATIC4_WHEEL_DRIVE = "automatic4WheelDrive"
    MANUAL = "manual"
    MANUAL4_WHEEL_DRIVE = "manual4WheelDrive"
