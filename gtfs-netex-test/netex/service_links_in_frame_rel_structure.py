from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_link import ServiceLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceLinksInFrame_RelStructure"

    service_link: list[ServiceLink] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
