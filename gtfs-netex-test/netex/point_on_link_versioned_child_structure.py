from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.activation_point import ActivationPoint
from netex.activation_point_ref import ActivationPointRef
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.beacon_point import BeaconPoint
from netex.beacon_point_ref import BeaconPointRef
from netex.border_point import BorderPoint
from netex.border_point_ref import BorderPointRef
from netex.fare_scheduled_stop_point import FareScheduledStopPoint
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point import GaragePoint
from netex.garage_point_ref import GaragePointRef
from netex.link_ref_structure import LinkRefStructure
from netex.multilingual_string import MultilingualString
from netex.parking_point import ParkingPoint
from netex.parking_point_ref import ParkingPointRef
from netex.path_junction import PathJunction
from netex.point_2 import Point2
from netex.point_ref import PointRef
from netex.railway_junction import RailwayJunction
from netex.railway_point_ref import RailwayPointRef
from netex.relief_point import ReliefPoint
from netex.relief_point_ref import ReliefPointRef
from netex.road_junction import RoadJunction
from netex.road_point_ref import RoadPointRef
from netex.route_point import RoutePoint
from netex.route_point_ref import RoutePointRef
from netex.scheduled_stop_point import ScheduledStopPoint
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.timing_point import TimingPoint
from netex.timing_point_ref import TimingPointRef
from netex.traffic_control_point import TrafficControlPoint
from netex.traffic_control_point_ref import TrafficControlPointRef
from netex.vehicle_meeting_point import VehicleMeetingPoint
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.wire_junction import WireJunction
from netex.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLinkVersionedChildStructure(VersionedChildStructure):
    """
    Type for a POINT ON LINK.

    :ivar name: Name of LINK.
    :ivar link_ref: Parent LINK -Can be omitted if given by context.
    :ivar distance_from_start: Distance of Point on Link from start of
        LINK.
    :ivar choice:
    :ivar order: Order of step in sequence
    """
    class Meta:
        name = "PointOnLink_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_from_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
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
                {
                    "name": "VehicleMeetingPoint",
                    "type": VehicleMeetingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPoint",
                    "type": BorderPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePoint",
                    "type": RoutePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPoint",
                    "type": TimingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPoint",
                    "type": TrafficControlPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Point",
                    "type": Point2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
