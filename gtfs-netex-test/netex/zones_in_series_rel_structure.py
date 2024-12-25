from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .zone_in_series_versioned_child_structure import ZoneInSeriesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZonesInSeriesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "zonesInSeries_RelStructure"

    zone_in_series: list[ZoneInSeriesVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "ZoneInSeries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
