from dataclasses import dataclass, field
from netex.capping_rule_price_versioned_child_structure import CappingRulePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CappingRulePrice(CappingRulePriceVersionedChildStructure):
    """
    A set of all possible price features of a CAPPING RULE default total price,
    discount in value or percentage etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
