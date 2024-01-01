from dataclasses import dataclass
from .booking_policy_ref_structure import BookingPolicyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservingRefStructure(BookingPolicyRefStructure):
    value: RestrictedVar
