from dataclasses import dataclass, field
from typing import List
from netex.booking_method_enumeration import BookingMethodEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BookingPolicyVersionStructure(UsageParameterVersionStructure):
    """
    Type for BOOKING POLICY.

    :ivar booking_methods: Booking methods allowed
    """
    class Meta:
        name = "BookingPolicy_VersionStructure"

    booking_methods: List[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
