from dataclasses import dataclass, field
from netex.pricing_rule_versioned_structure import PricingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingRule(PricingRuleVersionedStructure):
    """
    Parameters describing how a fare is to be computed.

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
