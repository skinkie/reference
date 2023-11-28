from dataclasses import dataclass, field
from netex.family_facility_enumeration import FamilyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FamilyFacility:
    """
    Classification of FAMILY FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FamilyFacilityEnumeration = field(
        default=FamilyFacilityEnumeration.NONE,
        metadata={
            "required": True,
        }
    )
