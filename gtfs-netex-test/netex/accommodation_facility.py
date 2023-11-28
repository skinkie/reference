from dataclasses import dataclass, field
from netex.accommodation_facility_enumeration import AccommodationFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccommodationFacility:
    """Classification of ACCOMMODATION FACILITY type - TPEG pti23."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccommodationFacilityEnumeration = field(
        default=AccommodationFacilityEnumeration.SEATING,
        metadata={
            "required": True,
        }
    )
