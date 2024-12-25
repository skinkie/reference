from dataclasses import dataclass, field

from .sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
