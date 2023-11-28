from dataclasses import dataclass, field
from netex.assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceFacility:
    """
    Classification of ASSISTANCE FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AssistanceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
