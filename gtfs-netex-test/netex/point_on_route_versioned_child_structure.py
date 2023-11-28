from dataclasses import dataclass, field
from typing import Optional
from netex.activation_point_ref import ActivationPointRef
from netex.beacon_point_ref import BeaconPointRef
from netex.border_point_ref import BorderPointRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point_ref import GaragePointRef
from netex.parking_point_ref import ParkingPointRef
from netex.point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from netex.point_ref import PointRef
from netex.railway_point_ref import RailwayPointRef
from netex.relief_point_ref import ReliefPointRef
from netex.road_point_ref import RoadPointRef
from netex.route_instructions_rel_structure import RouteInstructionsRelStructure
from netex.route_link_ref_structure import RouteLinkRefStructure
from netex.route_point_ref import RoutePointRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.timing_point_ref import TimingPointRef
from netex.traffic_control_point_ref import TrafficControlPointRef
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnRouteVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    """
    Type for a POINT ON ROUTE.

    :ivar choice_1:
    :ivar onward_route_link_ref: Optional Reference to onward link to
        use - can be used to disambiguate where there are multiple links
        between the same point.
    :ivar route_instructions: Instructins for following route. +v1.1
    """
    class Meta:
        name = "PointOnRoute_VersionedChildStructure"

    choice_1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
    onward_route_link_ref: Optional[RouteLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardRouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_instructions: Optional[RouteInstructionsRelStructure] = field(
        default=None,
        metadata={
            "name": "routeInstructions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
