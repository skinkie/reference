from dataclasses import dataclass, field
from typing import List
from netex.capping_rule_price import CappingRulePrice
from netex.capping_rule_price_ref import CappingRulePriceRef
from netex.cell_ref import CellRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CappingRulePricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CAPPING RULE PRICEs.
    """
    class Meta:
        name = "cappingRulePrices_RelStructure"

    capping_rule_price_ref_or_cell_ref_or_capping_rule_price: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
