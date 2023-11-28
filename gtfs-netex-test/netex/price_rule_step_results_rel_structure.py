from dataclasses import dataclass, field
from typing import List
from netex.price_rule_step_result_structure import PriceRuleStepResultStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PriceRuleStepResultsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of rules step calculation results.

    :ivar rule_step_result: Record of amount deducted by a price rule
        calculation, e.g. an additional tax step. If PRICING RULES are
        chained there may be multiple steps to record. The source of the
        input price can be indicated by a FARE PRICE REF of some sort.
        The RULE STEP RESULT Amount is the resulting  net price after
        the pricing rule has been applied to the input amount. The RULE
        STEP RESULT  Adjustment Amount is  the difference beteen the
        original input price and the RULE STEP RESULT  Amount (so it is
        possible to derive the input price amount  by adding the the
        Adjustment to the  Net Amount.  A similar computation can be
        done for any units.
    """
    class Meta:
        name = "priceRuleStepResults_RelStructure"

    rule_step_result: List[PriceRuleStepResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "RuleStepResult",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
