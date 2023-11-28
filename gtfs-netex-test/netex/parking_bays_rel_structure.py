from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.monitored_vehicle_sharing_parking_bay import MonitoredVehicleSharingParkingBay
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.parking_bay import ParkingBay
from netex.parking_bay_ref import ParkingBayRef
from netex.vehicle_pooling_parking_bay import VehiclePoolingParkingBay
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_sharing_parking_bay import VehicleSharingParkingBay
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING BAYs.
    """
    class Meta:
        name = "parkingBays_RelStructure"

    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "MonitoredVehicleSharingParkingBay",
                    "type": MonitoredVehicleSharingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingBay",
                    "type": VehiclePoolingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBay",
                    "type": VehicleSharingParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBay",
                    "type": ParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
