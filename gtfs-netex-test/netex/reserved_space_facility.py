from dataclasses import dataclass, field
from netex.reserved_space_facility_enumeration import ReservedSpaceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReservedSpaceFacility:
    """
    Classification of RESERVED SPACE FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
