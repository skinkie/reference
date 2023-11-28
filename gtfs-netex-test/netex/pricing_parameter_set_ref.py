from dataclasses import dataclass
from netex.pricing_parameter_set_ref_structure import PricingParameterSetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingParameterSetRef(PricingParameterSetRefStructure):
    """
    Reference to a PRICING PARAMETERS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
