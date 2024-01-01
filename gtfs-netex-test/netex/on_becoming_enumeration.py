from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnBecomingEnumeration(Enum):
    AUTOMATIC = "automatic"
    INVITE = "invite"
    NO_ACTION = "noAction"
    OTHER = "other"
