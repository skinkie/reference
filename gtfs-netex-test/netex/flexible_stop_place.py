from dataclasses import dataclass

from .flexible_stop_place_version_structure import FlexibleStopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleStopPlace(FlexibleStopPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
