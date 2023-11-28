from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.pricing_rule_versioned_structure import PricingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DiscountingRuleVersionedStructure(PricingRuleVersionedStructure):
    """
    Type for DISCOUNTING RULE.

    :ivar discount_as_percentage: Discount as a percentage of the full
        price.
    :ivar discount_as_value: Discount amount. i.e. DIfference between
        full and discounted price.
    :ivar can_be_cumulative: Whether this discount can be used
        cumulatively with other discounts.
    """
    class Meta:
        name = "DiscountingRule_VersionedStructure"

    discount_as_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DiscountAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discount_as_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DiscountAsValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_be_cumulative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeCumulative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
