from dataclasses import dataclass, field
from typing import Optional
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.parking_bay_ref import ParkingBayRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_service_place_assignment_version_structure import VehicleServicePlaceAssignmentVersionStructure
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServicePlaceAssignmentVersionStructure(VehicleServicePlaceAssignmentVersionStructure):
    """
    Type for TAXI SERVICE PLACE ASSIGNMENT restricts id.
    """
    class Meta:
        name = "TaxiServicePlaceAssignment_VersionStructure"

    taxi_service_ref: TaxiServiceRef = field(
        metadata={
            "name": "TaxiServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    taxi_parking_area_ref: Optional[TaxiParkingAreaRef] = field(
        default=None,
        metadata={
            "name": "TaxiParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    taxi_stand_ref: Optional[TaxiStandRef] = field(
        default=None,
        metadata={
            "name": "TaxiStandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
