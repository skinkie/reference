from dataclasses import dataclass, field

from .nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NuisanceFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: NuisanceFacilityEnumeration = field(
        default=NuisanceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
