from dataclasses import dataclass, field
from typing import Iterable

from .containment_aggregation_structure import ContainmentAggregationStructure
from .default_interchange import DefaultInterchange

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultInterchangesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "defaultInterchangesInFrame_RelStructure"

    default_interchange: Iterable[DefaultInterchange] = field(
        default_factory=list,
        metadata={
            "name": "DefaultInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
