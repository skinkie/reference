from dataclasses import dataclass
from netex.road_address_ref_structure import RoadAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadAddressRef(RoadAddressRefStructure):
    """
    Reference to a Road ADDRESS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
