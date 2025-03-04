from dataclasses import dataclass, field

from .booking_method_enumeration import BookingMethodEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BookingPolicyVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "BookingPolicy_VersionStructure"

    booking_methods: list[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
