from dataclasses import dataclass, field

from .medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MedicalFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
