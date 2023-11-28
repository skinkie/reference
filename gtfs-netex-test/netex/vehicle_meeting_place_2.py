from dataclasses import dataclass
from netex.addressable_place_version_structure import AddressablePlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPlace2(AddressablePlaceVersionStructure):
    """
    DUMMY type to workaround SG limitation.
    """
    class Meta:
        name = "VehicleMeetingPlace_"
        namespace = "http://www.netex.org.uk/netex"
