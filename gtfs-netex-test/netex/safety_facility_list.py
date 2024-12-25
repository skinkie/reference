from dataclasses import dataclass, field

from .safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SafetyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
