from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .operational_context import OperationalContext

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperationalContextsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operationalContextsInFrame_RelStructure"

    operational_context: list[OperationalContext] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
