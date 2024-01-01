from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReasonForMeetingEnumeration(Enum):
    SERVICE_FACILITY = "serviceFacility"
    JOINING = "joining"
    TARIFF_SECTION = "tariffSection"
    SPLITTING = "splitting"
