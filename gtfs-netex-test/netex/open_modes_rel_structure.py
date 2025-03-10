from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .open_transport_mode import OpenTransportMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OpenModesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "openModesRelStructure"

    open_transport_mode: list[OpenTransportMode] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
