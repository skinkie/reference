from dataclasses import dataclass

from .road_address_ref_structure import RoadAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoadAddressRef(RoadAddressRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
