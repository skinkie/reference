from dataclasses import dataclass, field
from typing import Optional
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.parking_bay_ref import ParkingBayRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_service_place_assignment_version_structure import VehicleServicePlaceAssignmentVersionStructure
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingPlaceAssignmentVersionStructure(VehicleServicePlaceAssignmentVersionStructure):
    """
    Type for VEHICLE POOLING PLACE ASSIGNMENT restricts id.
    """
    class Meta:
        name = "VehiclePoolingPlaceAssignment_VersionStructure"

    chauffeured_vehicle_service_ref_or_taxi_service_ref_or_car_pooling_service_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
    vehicle_pooling_meeting_place_ref_or_vehicle_pooling_parking_area_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingMeetingPlaceRef",
                    "type": VehiclePoolingMeetingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
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
