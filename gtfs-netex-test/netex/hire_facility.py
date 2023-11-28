from dataclasses import dataclass, field
from netex.hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HireFacility:
    """
    Classification of Hire FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: HireFacilityEnumeration = field(
        default=HireFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
