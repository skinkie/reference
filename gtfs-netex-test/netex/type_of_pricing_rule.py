from dataclasses import dataclass, field
from netex.type_of_pricing_rule_version_structure import TypeOfPricingRuleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPricingRule(TypeOfPricingRuleVersionStructure):
    """Classification of pricing rule.

    Can be used for VAT categories, etc.  +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
