from dataclasses import dataclass, field
from typing import List
from netex.money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MoneyFacilityList:
    """
    List of MONEY FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MoneyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
