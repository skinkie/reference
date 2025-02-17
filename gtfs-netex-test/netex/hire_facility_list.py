from dataclasses import dataclass, field

from .hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HireFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
