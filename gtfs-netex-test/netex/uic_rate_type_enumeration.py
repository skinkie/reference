from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UicRateTypeEnumeration(Enum):
    NORMAL = "normal"
    DISCOUNT_IN_TRAIN_OTHER_THAN_TGV = "discountInTrainOtherThanTGV"
    SPECIAL_FARE = "specialFare"
    SUPPLEMENT = "supplement"
    NO_PUBLISHED_TARIFF = "noPublishedTariff"
