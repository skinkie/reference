from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .monitored_vehicle_sharing_parking_bay import MonitoredVehicleSharingParkingBay
from .monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from .parking_bay import ParkingBay
from .parking_bay_ref import ParkingBayRef
from .vehicle_pooling_parking_bay import VehiclePoolingParkingBay
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_sharing_parking_bay import VehicleSharingParkingBay
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingBaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingBays_RelStructure"

    parking_bay_ref_or_vehicle_sharing_parking_bay_ref_or_parking_bay: list[Union[VehiclePoolingParkingBayRef, MonitoredVehicleSharingParkingBayRef, VehicleSharingParkingBayRef, ParkingBayRef, MonitoredVehicleSharingParkingBay, VehiclePoolingParkingBay, VehicleSharingParkingBay, ParkingBay]] = field(
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
        },
    )
