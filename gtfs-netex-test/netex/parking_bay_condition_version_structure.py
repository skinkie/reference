from dataclasses import dataclass, field
from typing import Optional
from netex.log_entry_version_structure import LogEntryVersionStructure
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.parking_bay_ref import ParkingBayRef
from netex.parking_bay_status_enumeration import ParkingBayStatusEnumeration
from netex.parking_bay_status_ref import ParkingBayStatusRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayConditionVersionStructure(LogEntryVersionStructure):
    """
    Type for a PARKING BAY CONDITION..

    :ivar choice:
    :ivar status: Current status
    :ivar parking_bay_status_ref:
    """
    class Meta:
        name = "ParkingBayCondition_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingBayRef",
                    "type": VehiclePoolingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBayRef",
                    "type": MonitoredVehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBayRef",
                    "type": VehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayRef",
                    "type": ParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
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
