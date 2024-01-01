from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceAttentionEnumeration(Enum):
    NONE = "none"
    DOORBELL = "doorbell"
    HELP_POINT = "helpPoint"
    INTERCOM = "intercom"
    OTHER = "other"
