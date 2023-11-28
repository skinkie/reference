from dataclasses import dataclass, field
from netex.retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailFacility:
    """
    Classification of RETAIL FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
