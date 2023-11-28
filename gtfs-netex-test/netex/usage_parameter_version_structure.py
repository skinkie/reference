from dataclasses import dataclass, field
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from netex.usage_parameter_prices_rel_structure import UsageParameterPricesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageParameterVersionStructure(PriceableObjectVersionStructure):
    """
    Type for USAGE PARAMETER.

    :ivar type_of_usage_parameter_ref:
    :ivar prices: Prices associated with USAGE PARAMETER.
    """
    class Meta:
        name = "UsageParameter_VersionStructure"

    type_of_usage_parameter_ref: Optional[TypeOfUsageParameterRef] = field(
        default=None,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[UsageParameterPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
