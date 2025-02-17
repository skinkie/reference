from dataclasses import dataclass

from .pricing_parameter_set_versioned_structure import PricingParameterSetVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PricingParameterSet(PricingParameterSetVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
