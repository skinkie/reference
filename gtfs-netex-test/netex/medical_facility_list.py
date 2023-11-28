from dataclasses import dataclass, field
from typing import List
from netex.medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MedicalFacilityList:
    """
    List of MEDICAL FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
