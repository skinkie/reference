from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResidenceTypeEnumeration(Enum):
    LIVE = "live"
    WORK = "work"
    STUDY = "study"
    EXCHANGE = "exchange"
    BORN = "born"
    NON_RESIDENT = "nonResident"
