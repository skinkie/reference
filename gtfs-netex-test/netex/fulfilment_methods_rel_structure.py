from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fulfilment_method import FulfilmentMethod
from netex.fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FULFILMENT METHODs.
    """
    class Meta:
        name = "fulfilmentMethods_RelStructure"

    fulfilment_method_ref_or_fulfilment_method: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethod",
                    "type": FulfilmentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
