from dataclasses import dataclass

from .stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StopPlaceSpaceRef(StopPlaceSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
