from dataclasses import dataclass, field
from typing import List, Optional
from netex.activation_point_ref import ActivationPointRef
from netex.beacon_point_ref import BeaconPointRef
from netex.border_point_ref import BorderPointRef
from netex.complex_feature_ref_structure import ComplexFeatureRefStructure
from netex.complex_feature_refs_rel_structure import ComplexFeatureRefsRelStructure
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point_ref import GaragePointRef
from netex.parking_point_ref import ParkingPointRef
from netex.point_ref import PointRef
from netex.projection_version_structure import ProjectionVersionStructure
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
class ComplexFeatureProjectionVersionStructure(ProjectionVersionStructure):
    """
    Type for a COMPLEX FEATURE PROJECTION.

    :ivar projected_fearture_ref: COMPLEX FEATURE which is being
        projetced.
    :ivar onto_feature_ref: COMPLEX FEATURE onto which projection is
        being made.
    :ivar choice:
    :ivar features: COMPLEX FEATURES in PROJECTION.
    """
    class Meta:
        name = "ComplexFeatureProjection_VersionStructure"

    projected_fearture_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedFeartureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onto_feature_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "OntoFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
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
    features: Optional[ComplexFeatureRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
