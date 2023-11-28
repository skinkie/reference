from dataclasses import dataclass
from netex.booking_policy_ref_structure import BookingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CancellingRefStructure(BookingPolicyRefStructure):
    """
    Type for Reference to a CANCELLING USAGE PARAMETER.
    """
