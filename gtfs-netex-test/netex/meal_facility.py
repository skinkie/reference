from dataclasses import dataclass, field
from netex.meal_facility_enumeration import MealFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MealFacility:
    """
    Classification of MEAL FACILITY type.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MealFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
