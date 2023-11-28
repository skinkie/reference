from dataclasses import dataclass, field
from typing import Optional
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.parking_bay_ref import ParkingBayRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_service_place_assignment_version_structure import VehicleServicePlaceAssignmentVersionStructure
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingPlaceAssignmentVersionStructure(VehicleServicePlaceAssignmentVersionStructure):
    """
    Type for VEHICLE SHARING PLACE ASSIGNMENT restricts id.
    """
    class Meta:
        name = "VehicleSharingPlaceAssignment_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    vehicle_sharing_parking_area_ref: VehicleSharingParkingAreaRef = field(
        metadata={
            "name": "VehicleSharingParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    choice_1: Optional[object] = field(
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
