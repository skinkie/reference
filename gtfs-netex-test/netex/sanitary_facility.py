from dataclasses import dataclass, field
from netex.sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SanitaryFacility:
    """Classification of Sanitary FACILITY type - TPEG pti23."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SanitaryFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
