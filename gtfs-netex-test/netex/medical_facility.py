from dataclasses import dataclass, field
from .medical_facility_enumeration import MedicalFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MedicalFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MedicalFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
