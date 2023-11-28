from dataclasses import dataclass, field
from typing import Optional
from netex.parking_bay_status_enumeration import ParkingBayStatusEnumeration
from netex.parking_bay_status_ref import ParkingBayStatusRef
from netex.vehicle_sharing_parking_bay_version_structure import VehicleSharingParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonitoredVehicleSharingParkingBayVersionStructure(VehicleSharingParkingBayVersionStructure):
    """
    Type for MONITORED VEHICLE SHARING  PARKING BAY.

    :ivar status: Current status
    :ivar parking_bay_status_ref:
    """
    class Meta:
        name = "MonitoredVehicleSharingParkingBay_VersionStructure"

    status: Optional[ParkingBayStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay_status_ref: Optional[ParkingBayStatusRef] = field(
        default=None,
        metadata={
            "name": "ParkingBayStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
