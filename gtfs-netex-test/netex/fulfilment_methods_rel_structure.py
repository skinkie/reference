from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fulfilment_method import FulfilmentMethod
from .fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FulfilmentMethodsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fulfilmentMethods_RelStructure"

    fulfilment_method_ref_or_fulfilment_method: list[Union[FulfilmentMethodRef, FulfilmentMethod]] = field(
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
        },
    )
