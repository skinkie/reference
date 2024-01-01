from dataclasses import dataclass, field
from typing import List
from .medical_facility_enumeration import MedicalFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MedicalFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
