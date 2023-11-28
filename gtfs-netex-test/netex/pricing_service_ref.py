from dataclasses import dataclass
from netex.pricing_service_ref_structure import PricingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingServiceRef(PricingServiceRefStructure):
    """
    Reference to a PRICING SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
