from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_exclusion import ServiceExclusion

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceExclusionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceExclusionsInFrame_RelStructure"

    service_exclusion: list[ServiceExclusion] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
