from dataclasses import dataclass

from .occupancy_view_version_structure import OccupancyViewVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OccupancyView(OccupancyViewVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
