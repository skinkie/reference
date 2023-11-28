from dataclasses import dataclass, field
from netex.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Staffing:
    """
    Classification of STAFFING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: StaffingEnumeration = field(
        metadata={
            "required": True,
        }
    )
