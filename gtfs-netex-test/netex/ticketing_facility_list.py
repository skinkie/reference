from dataclasses import dataclass, field
from typing import List
from .ticketing_facility_enumeration import TicketingFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
