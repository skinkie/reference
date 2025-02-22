from dataclasses import dataclass

from .pricing_service_versioned_structure import PricingServiceVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PricingService(PricingServiceVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
