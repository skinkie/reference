from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fleet import Fleet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FleetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fleets_RelStructure"

    fleet: list[Fleet] = field(
        default_factory=list,
        metadata={
            "name": "Fleet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
