from dataclasses import dataclass

from .topographic_place_version_structure import TopographicPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TopographicPlace(TopographicPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
