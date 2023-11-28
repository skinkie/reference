from dataclasses import dataclass, field
from netex.monitored_vehicle_sharing_parking_bay_version_structure import MonitoredVehicleSharingParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonitoredVehicleSharingParkingBay(MonitoredVehicleSharingParkingBayVersionStructure):
    """A spot in the PARKING AREA dedicated to MONITORED VEHICLE SHARING  or
    rental.

    +v1.2.2

    :ivar id: Identifier of MONITORED VEHICLE SHARING PARKING BAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
