from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_pricing_rule_ref import TypeOfPricingRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPricingRuleRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF PRICING RULE.
    """
    class Meta:
        name = "TypeOfPricingRuleRefs_RelStructure"

    type_of_pricing_rule_ref: List[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
