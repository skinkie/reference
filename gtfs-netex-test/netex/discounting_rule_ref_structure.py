from dataclasses import dataclass
from .pricing_rule_ref_structure import PricingRuleRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountingRuleRefStructure(PricingRuleRefStructure):
    value: RestrictedVar
