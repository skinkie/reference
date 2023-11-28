from dataclasses import dataclass
from netex.point_of_interest_vehicle_entrance_ref_structure import PointOfInterestVehicleEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestVehicleEntranceRef(PointOfInterestVehicleEntranceRefStructure):
    """
    Reference to a POINT OF INTEREST VEHICLEENTRANCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
