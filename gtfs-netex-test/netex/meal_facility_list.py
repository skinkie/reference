from dataclasses import dataclass, field
from typing import List
from .meal_facility_enumeration import MealFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MealFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MealFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
