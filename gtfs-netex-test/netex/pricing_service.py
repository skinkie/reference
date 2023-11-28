from dataclasses import dataclass, field
from netex.pricing_service_versioned_structure import PricingServiceVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingService(PricingServiceVersionedStructure):
    """
    A web service used to provide prices dynamically at time of booking or
    purchase.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
