from dataclasses import dataclass, field
from netex.discounting_rule_versioned_structure import DiscountingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DiscountingRule(DiscountingRuleVersionedStructure):
    """
    A price for which a discount can be offered.

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
