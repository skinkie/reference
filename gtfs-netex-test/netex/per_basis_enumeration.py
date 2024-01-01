from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PerBasisEnumeration(Enum):
    PER_OFFER = "perOffer"
    PER_PERSON = "perPerson"
