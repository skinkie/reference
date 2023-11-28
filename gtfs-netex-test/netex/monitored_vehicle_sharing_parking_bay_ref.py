from dataclasses import dataclass
from netex.monitored_vehicle_sharing_parking_bay_ref_structure import MonitoredVehicleSharingParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonitoredVehicleSharingParkingBayRef(MonitoredVehicleSharingParkingBayRefStructure):
    """Reference to a MONITORED VEHICLE SHARING PARKING BAY.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
