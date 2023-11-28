from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeliveryVariantTypeEnumeration(Enum):
    """
    Allowed values for Notice delivery media type.
    """
    ANY = "any"
    PRINTED = "printed"
    TEXT_TO_SPEECH = "textToSpeech"
    RECORDED_ANNOUNCEMENT = "recordedAnnouncement"
    WEB = "web"
    MOBILE = "mobile"
    OTHER = "other"
