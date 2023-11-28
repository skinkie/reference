from dataclasses import dataclass, field
from typing import List, Optional
from netex.access_space_ref import AccessSpaceRef
from netex.address_ref import AddressRef
from netex.addressable_place_ref import AddressablePlaceRef
from netex.boarding_position_ref import BoardingPositionRef
from netex.entrance_ref import EntranceRef
from netex.equipment_place_ref import EquipmentPlaceRef
from netex.equipment_position_ref import EquipmentPositionRef
from netex.flexible_area_ref import FlexibleAreaRef
from netex.flexible_quay_ref import FlexibleQuayRef
from netex.flexible_stop_place_ref import FlexibleStopPlaceRef
from netex.garage_ref import GarageRef
from netex.hail_and_ride_area_ref import HailAndRideAreaRef
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.network_ref import NetworkRef
from netex.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.parking_area_ref import ParkingAreaRef
from netex.parking_bay_ref import ParkingBayRef
from netex.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.parking_entrance_ref import ParkingEntranceRef
from netex.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.parking_ref import ParkingRef
from netex.path_junction_ref import PathJunctionRef
from netex.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.postal_address_ref import PostalAddressRef
from netex.quay_ref import QuayRef
from netex.road_address_ref import RoadAddressRef
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
from netex.topographic_place_ref import TopographicPlaceRef
from netex.vehicle_entrance_ref import VehicleEntranceRef
from netex.vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from netex.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from netex.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkFilterByValueStructure(ObjectFilterByValueStructure):
    """
    Specifies values to filter by reference value, rather than frame.

    :ivar network_ref:
    :ivar places: Return all site elements for given place.
    """
    network_ref: Optional[NetworkRef] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    places: Optional["NetworkFilterByValueStructure.Places"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Places:
        choice: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "HailAndRideAreaRef",
                        "type": HailAndRideAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleAreaRef",
                        "type": FlexibleAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleQuayRef",
                        "type": FlexibleQuayRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleStopPlaceRef",
                        "type": FlexibleStopPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "PathJunctionRef",
                        "type": PathJunctionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "EquipmentPlaceRef",
                        "type": EquipmentPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "EquipmentPositionRef",
                        "type": EquipmentPositionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "TopographicPlaceRef",
                        "type": TopographicPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
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
                    {
                        "name": "PostalAddressRef",
                        "type": PostalAddressRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "RoadAddressRef",
                        "type": RoadAddressRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "AddressRef",
                        "type": AddressRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            }
        )
