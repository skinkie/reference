from dataclasses import dataclass

from .stop_place_ref_structure import StopPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StopPlaceRef(StopPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
