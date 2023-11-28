from dataclasses import dataclass, field
from netex.mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityFacility:
    """
    Classification of MOBILITY FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MobilityFacilityEnumeration = field(
        default=MobilityFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
