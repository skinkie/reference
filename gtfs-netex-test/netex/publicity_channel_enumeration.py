from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PublicityChannelEnumeration(Enum):
    ALL = "all"
    PRINTED_MEDIA = "printedMedia"
    DYNAMIC_MEDIA = "dynamicMedia"
    NONE = "none"
