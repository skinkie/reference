from dataclasses import dataclass

from .booking_policy_ref_structure import BookingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BookingPolicyRef(BookingPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
