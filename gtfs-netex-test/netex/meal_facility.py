from dataclasses import dataclass, field
from .meal_facility_enumeration import MealFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MealFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MealFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
