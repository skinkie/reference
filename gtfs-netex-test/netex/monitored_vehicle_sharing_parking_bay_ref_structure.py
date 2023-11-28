from dataclasses import dataclass
from netex.vehicle_sharing_parking_bay_ref_structure import VehicleSharingParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonitoredVehicleSharingParkingBayRefStructure(VehicleSharingParkingBayRefStructure):
    """
    Type for a reference to a MONITORED VEHICLE SHARING PARKING BAY.
    """
