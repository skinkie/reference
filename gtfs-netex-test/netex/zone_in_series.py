from dataclasses import dataclass, field

from .zone_in_series_versioned_child_structure import ZoneInSeriesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneInSeries(ZoneInSeriesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
