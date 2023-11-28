from dataclasses import dataclass, field
from typing import List
from netex.access_space import AccessSpace
from netex.access_zone import AccessZone
from netex.addressable_place import AddressablePlace
from netex.administrative_zone_version_structure import (
    AdministrativeZone,
    TransportAdministrativeZone,
)
from netex.boarding_position import BoardingPosition
from netex.cell_versioned_child_structure import (
    FareTable,
    FareTableInContext,
    PriceGroup,
)
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.country import Country
from netex.crew_base import CrewBase
from netex.entrance import Entrance
from netex.equipment_place import EquipmentPlace
from netex.fare_zone import FareZone
from netex.flexible_area import FlexibleArea
from netex.flexible_quay import FlexibleQuay
from netex.flexible_stop_place import FlexibleStopPlace
from netex.garage import Garage
from netex.general_group_of_entities import GeneralGroupOfEntities
from netex.general_zone import GeneralZone
from netex.group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from netex.group_of_distribution_channels import GroupOfDistributionChannels
from netex.group_of_lines import GroupOfLines
from netex.group_of_link_sequences import GroupOfLinkSequences
from netex.group_of_links import GroupOfLinks
from netex.group_of_operators import GroupOfOperators
from netex.group_of_places import GroupOfPlaces
from netex.group_of_points import GroupOfPoints
from netex.group_of_services import GroupOfServices
from netex.group_of_single_journeys import GroupOfSingleJourneys
from netex.group_of_timing_links import GroupOfTimingLinks
from netex.hail_and_ride_area import HailAndRideArea
from netex.headway_journey_group import HeadwayJourneyGroup
from netex.layer import Layer
from netex.mobility_service_constraint_zone import MobilityServiceConstraintZone
from netex.monitored_vehicle_sharing_parking_bay import MonitoredVehicleSharingParkingBay
from netex.network import Network
from netex.parking import Parking
from netex.parking_area import ParkingArea
from netex.parking_bay import ParkingBay
from netex.parking_component import ParkingComponent
from netex.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from netex.parking_passenger_entrance import ParkingPassengerEntrance
from netex.point_of_interest import PointOfInterest
from netex.point_of_interest_entrance import PointOfInterestEntrance
from netex.point_of_interest_space import PointOfInterestSpace
from netex.point_of_interest_vehicle_entrance import PointOfInterestVehicleEntrance
from netex.pool_of_vehicles import PoolOfVehicles
from netex.postal_address import PostalAddress
from netex.quay import Quay
from netex.rhythmical_journey_group import RhythmicalJourneyGroup
from netex.road_address import RoadAddress
from netex.routing_constraint_zone import RoutingConstraintZone
from netex.service_site import ServiceSite
from netex.standard_fare_table import StandardFareTable
from netex.stop_area import StopArea
from netex.stop_place import StopPlace
from netex.stop_place_entrance import StopPlaceEntrance
from netex.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from netex.tariff_zone import TariffZone
from netex.taxi_parking_area import TaxiParkingArea
from netex.taxi_rank import TaxiRank
from netex.taxi_stand import TaxiStand
from netex.topographic_place import TopographicPlace
from netex.vehicle_meeting_place_1 import VehicleMeetingPlace1
from netex.vehicle_meeting_place_2 import VehicleMeetingPlace2
from netex.vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace
from netex.vehicle_pooling_parking_area import VehiclePoolingParkingArea
from netex.vehicle_pooling_parking_bay import VehiclePoolingParkingBay
from netex.vehicle_sharing_parking_area import VehicleSharingParkingArea
from netex.vehicle_sharing_parking_bay import VehicleSharingParkingBay
from netex.vehicle_stopping_place import VehicleStoppingPlace
from netex.vehicle_stopping_position import VehicleStoppingPosition
from netex.zone import Zone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfEntitiesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF ENTITIes.
    """
    class Meta:
        name = "groupOfEntitiesInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PoolOfVehicles",
                    "type": PoolOfVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSingleJourneys",
                    "type": GroupOfSingleJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannels",
                    "type": GroupOfDistributionChannels,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElements",
                    "type": GroupOfDistanceMatrixElements,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup",
                    "type": PriceGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServices",
                    "type": GroupOfServices,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrewBase",
                    "type": CrewBase,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimingLinks",
                    "type": GroupOfTimingLinks,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Network",
                    "type": Network,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLines",
                    "type": GroupOfLines,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperators",
                    "type": GroupOfOperators,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPlaces",
                    "type": GroupOfPlaces,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinkSequences",
                    "type": GroupOfLinkSequences,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceConstraintZone",
                    "type": MobilityServiceConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingConstraintZone",
                    "type": RoutingConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopArea",
                    "type": StopArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZone",
                    "type": AccessZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace",
                    "type": VehicleMeetingPlace1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingMeetingPlace",
                    "type": VehiclePoolingMeetingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace_",
                    "type": VehicleMeetingPlace2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideArea",
                    "type": HailAndRideArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleArea",
                    "type": FlexibleArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlace",
                    "type": FlexibleStopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Garage",
                    "type": Garage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiStand",
                    "type": TaxiStand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlace",
                    "type": VehicleStoppingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingComponent",
                    "type": ParkingComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPosition",
                    "type": VehicleStoppingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingArea",
                    "type": VehiclePoolingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingArea",
                    "type": VehicleSharingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingArea",
                    "type": TaxiParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea,
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
                {
                    "name": "PointOfInterestVehicleEntrance",
                    "type": PointOfInterestVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntrance",
                    "type": PointOfInterestEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntrance",
                    "type": ParkingPassengerEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehicles",
                    "type": ParkingEntranceForVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntrance",
                    "type": StopPlaceVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntrance",
                    "type": StopPlaceEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Entrance",
                    "type": Entrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterest",
                    "type": PointOfInterest,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Parking",
                    "type": Parking,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiRank",
                    "type": TaxiRank,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSite",
                    "type": ServiceSite,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlace",
                    "type": TopographicPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Country",
                    "type": Country,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressablePlace",
                    "type": AddressablePlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": TransportAdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": AdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZone",
                    "type": FareZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZone",
                    "type": TariffZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralZone",
                    "type": GeneralZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Zone",
                    "type": Zone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinks",
                    "type": GroupOfLinks,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPoints",
                    "type": GroupOfPoints,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Layer",
                    "type": Layer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
