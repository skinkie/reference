from dataclasses import dataclass, field
from typing import List

from .passenger_information_facility_enumeration import (
    PassengerInformationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[PassengerInformationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
