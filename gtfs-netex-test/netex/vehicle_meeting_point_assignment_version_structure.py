from dataclasses import dataclass, field
from typing import Optional
from netex.access_space_ref import AccessSpaceRef
from netex.addressable_place_ref import AddressablePlaceRef
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.boarding_position_ref import BoardingPositionRef
from netex.entrance_ref import EntranceRef
from netex.garage_ref import GarageRef
from netex.meeting_usage_enumeration import MeetingUsageEnumeration
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.parking_area_ref import ParkingAreaRef
from netex.parking_bay_ref import ParkingBayRef
from netex.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.parking_entrance_ref import ParkingEntranceRef
from netex.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.parking_ref import ParkingRef
from netex.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.quay_ref import QuayRef
from netex.service_site_ref import ServiceSiteRef
from netex.site_component_ref import SiteComponentRef
from netex.site_element_ref import SiteElementRef
from netex.site_ref import SiteRef
from netex.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.stop_place_ref import StopPlaceRef
from netex.stop_place_space_ref import StopPlaceSpaceRef
from netex.stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.vehicle_entrance_ref import VehicleEntranceRef
from netex.vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from netex.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for VEHICLE MEETING POINT ASSIGNMENT restricts id.
    """
    class Meta:
        name = "VehicleMeetingPointAssignment_VersionStructure"

    vehicle_meeting_point_ref: VehicleMeetingPointRef = field(
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    choice: Optional[object] = field(
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
                    "name": "VehicleMeetingPlaceRef",
                    "type": VehicleMeetingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GarageRef",
                    "type": GarageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPositionRef",
                    "type": VehicleStoppingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlaceRef",
                    "type": VehicleStoppingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceSpaceRef",
                    "type": StopPlaceSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": PointOfInterestSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntranceRef",
                    "type": StopPlaceVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntranceRef",
                    "type": StopPlaceEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntranceRef",
                    "type": ParkingPassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceRef",
                    "type": ParkingEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestVehicleEntranceRef",
                    "type": PointOfInterestVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": PointOfInterestEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEntranceRef",
                    "type": VehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceRef",
                    "type": EntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteComponentRef",
                    "type": SiteComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteElementRef",
                    "type": SiteElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressablePlaceRef",
                    "type": AddressablePlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    usage: Optional[MeetingUsageEnumeration] = field(
        default=None,
        metadata={
            "name": "Usage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
