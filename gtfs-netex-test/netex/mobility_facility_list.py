from dataclasses import dataclass, field

from .mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MobilityFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
