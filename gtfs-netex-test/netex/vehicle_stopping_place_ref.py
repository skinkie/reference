from dataclasses import dataclass
from netex.vehicle_stopping_place_ref_structure import VehicleStoppingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPlaceRef(VehicleStoppingPlaceRefStructure):
    """
    Reference to a VEHICLE STOPPING PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
