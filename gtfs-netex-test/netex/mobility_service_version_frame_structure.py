from dataclasses import dataclass, field
from typing import Optional
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.fleets_rel_structure import FleetsRelStructure
from netex.mobility_service_constraint_zones_in_frame_rel_structure import MobilityServiceConstraintZonesInFrameRelStructure
from netex.mobility_services_rel_structure import MobilityServicesRelStructure
from netex.modes_of_operation_rel_structure import ModesOfOperationRelStructure
from netex.online_services_rel_structure import OnlineServicesRelStructure
from netex.pool_of_vehicles_rel_structure import PoolOfVehiclesRelStructure
from netex.vehicle_meeting_links_in_frame_rel_structure import VehicleMeetingLinksInFrameRelStructure
from netex.vehicle_meeting_places_rel_structure import VehicleMeetingPlacesRelStructure
from netex.vehicle_meeting_point_assignments_in_frame_rel_structure import VehicleMeetingPointAssignmentsInFrameRelStructure
from netex.vehicle_meeting_points_in_frame_rel_structure import VehicleMeetingPointsInFrameRelStructure
from netex.vehicle_service_place_assignments_rel_structure import VehicleServicePlaceAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a MOBILITY SERVICE FRAME.

    :ivar fleets: FLEETs in Frame
    :ivar pools_of_vehicles: POOLs OF VEHICLEs in Frame
    :ivar modes_of_operation: MODEs of OPERATION
    :ivar mobility_services: MOBILITY SERVICEs in frame.
    :ivar online_services: ONLINE  SERVICEs in frame.
    :ivar vehicle_meeting_points: VEHICLE MEETING POINTs in frame.
    :ivar vehicle_meeting_links: VEHICLE MEETING POINTs in frame.
    :ivar vehicle_meeting_point_assignments: VEHICLE MEETING POINT
        ASSIGNMENTs in frame.
    :ivar vehicle_meeting_places: VEHICLE MEETIN.G PLACES  in frame.
    :ivar vehicle_meeting_place_assignments: VEHICLE SERVICE PLACE
        ASSIGNMENTs in frame.
    :ivar mobility_service_constraint_zones: Zone use restrictions in
        FRAME.
    """
    class Meta:
        name = "MobilityService_VersionFrameStructure"

    fleets: Optional[FleetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pools_of_vehicles: Optional[PoolOfVehiclesRelStructure] = field(
        default=None,
        metadata={
            "name": "poolsOfVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    modes_of_operation: Optional[ModesOfOperationRelStructure] = field(
        default=None,
        metadata={
            "name": "modesOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobility_services: Optional[MobilityServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "mobilityServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    online_services: Optional[OnlineServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "onlineServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_meeting_points: Optional[VehicleMeetingPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_meeting_links: Optional[VehicleMeetingLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_meeting_point_assignments: Optional[VehicleMeetingPointAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPointAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_meeting_places: Optional[VehicleMeetingPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_meeting_place_assignments: Optional[VehicleServicePlaceAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleMeetingPlaceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobility_service_constraint_zones: Optional[MobilityServiceConstraintZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "mobilityServiceConstraintZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
