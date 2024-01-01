from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TemplateVehicleJourneyTypeEnumeration(Enum):
    HEADWAY = "headway"
    RHYTHMIC = "rhythmic"
    OTHER = "other"
