from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.discounting_rule_versioned_structure import DiscountingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LimitingRuleVersionedStructure(DiscountingRuleVersionedStructure):
    """
    Type for LIMITING RULE.

    :ivar minimum_price: Maximum price at which to cap discounted fare.
    :ivar minimum_price_as_percentage: Minumum price as percentage of
        whole price.
    :ivar minimum_price_as_multiple: Minimum price as a number of single
        flat fares.
    :ivar maximum_price: Minimum amount at which to cap discounted fare.
    :ivar maximum_price_as_percentage: Maxumum price as percentage of
        whole price.
    :ivar maximum_price_as_multiple: Maximum price as a number of single
        flat fares.
    :ivar minimum_limit_price_as_percentage: Minimum Limit as percentage
        of whole price.
    :ivar minimum_limit_price: Limiting amount below which resulting
        fare may not be sold.
    :ivar maximum_limit_price_as_percentage: Maxumum Limit as percentage
        of whole price.
    :ivar maximum_limit_price: Limiting amount above which resulting
        fare may not be sold.
    """
    class Meta:
        name = "LimitingRule_VersionedStructure"

    minimum_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_price_as_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_price_as_multiple: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumPriceAsMultiple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_price_as_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_price_as_multiple: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPriceAsMultiple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_limit_price_as_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumLimitPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_limit_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumLimitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_limit_price_as_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumLimitPriceAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_limit_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumLimitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
