from dataclasses import dataclass
from .pricing_service_ref_structure import PricingServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingServiceRef(PricingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
