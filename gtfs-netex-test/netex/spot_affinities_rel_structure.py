from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .spot_affinity import SpotAffinity

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SpotAffinitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "spotAffinities_RelStructure"

    spot_affinity: list[SpotAffinity] = field(
        default_factory=list,
        metadata={
            "name": "SpotAffinity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
