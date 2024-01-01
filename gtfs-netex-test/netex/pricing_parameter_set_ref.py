from dataclasses import dataclass
from .pricing_parameter_set_ref_structure import (
    PricingParameterSetRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingParameterSetRef(PricingParameterSetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
