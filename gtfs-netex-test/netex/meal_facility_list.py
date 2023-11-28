from dataclasses import dataclass, field
from typing import List
from netex.meal_facility_enumeration import MealFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MealFacilityList:
    """
    List of MEAL FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MealFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
