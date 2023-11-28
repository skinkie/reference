from dataclasses import dataclass, field
from typing import Optional
from netex.activation_point_ref import ActivationPointRef
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.beacon_point_ref import BeaconPointRef
from netex.border_point_ref import BorderPointRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point_ref import GaragePointRef
from netex.parking_point_ref import ParkingPointRef
from netex.point_on_route_ref import PointOnRouteRef
from netex.point_ref import PointRef
from netex.railway_point_ref import RailwayPointRef
from netex.relief_point_ref import ReliefPointRef
from netex.road_point_ref import RoadPointRef
from netex.route_point_ref import RoutePointRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.timing_point_ref import TimingPointRef
from netex.traffic_control_point_ref import TrafficControlPointRef
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexiblePointPropertiesVersionedChildStructure(VersionedChildStructure):
    """
    Type for FLEXIBLE POINT PROPERTies.

    :ivar choice:
    :ivar may_be_skipped: Whether the POINT may be skipped.
    :ivar on_main_route: Whether the POINT is on the main ROUTE.
    :ivar point_standing_for_azone: Whether the POINT represents a
        FLEXIBLE ZONE.
    :ivar zone_containing_stops: Whether the ZONE is defined by a GROUP
        of POINT (true) or a geographical zone defined by its boundary.
    """
    class Meta:
        name = "FlexiblePointProperties_VersionedChildStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOnRouteRef",
                    "type": PointOnRouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointRef",
                    "type": VehicleMeetingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WirePointRef",
                    "type": WirePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadPointRef",
                    "type": RoadPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayPointRef",
                    "type": RailwayPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPointRef",
                    "type": TrafficControlPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPointRef",
                    "type": BeaconPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPointRef",
                    "type": ActivationPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePointRef",
                    "type": RoutePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    may_be_skipped: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MayBeSkipped",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    on_main_route: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnMainRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_standing_for_azone: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PointStandingForAZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_containing_stops: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZoneContainingStops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
