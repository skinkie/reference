from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeliveryVariantTypeEnumeration(Enum):
    ANY = "any"
    PRINTED = "printed"
    TEXT_TO_SPEECH = "textToSpeech"
    RECORDED_ANNOUNCEMENT = "recordedAnnouncement"
    WEB = "web"
    MOBILE = "mobile"
    OTHER = "other"
