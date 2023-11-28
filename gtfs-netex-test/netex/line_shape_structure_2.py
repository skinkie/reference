from dataclasses import dataclass, field
from typing import Optional
from netex.activation_link_ref import ActivationLinkRef
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.line_link_ref import LineLinkRef
from netex.multilingual_string import MultilingualString
from netex.onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from netex.path_link_ref import PathLinkRef
from netex.railway_link_ref import RailwayLinkRef
from netex.road_link_ref import RoadLinkRef
from netex.route_link_ref import RouteLinkRef
from netex.service_link_ref import ServiceLinkRef
from netex.timing_link_ref import TimingLinkRef
from netex.vehicle_meeting_link_ref import VehicleMeetingLinkRef
from netex.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineShapeStructure2(DataManagedObjectStructure):
    """
    Type for a LINE SHAPE.

    :ivar formula: Formula for calculating line.
    :ivar name: Name of LINE SHAPE.
    :ivar choice:
    :ivar locating_system_ref: Name of locating system under which line
        is specified.
    """
    class Meta:
        name = "LineShapeStructure"

    formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "Formula",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
                    "name": "OnwardVehicleMeetingLinkRef",
                    "type": OnwardVehicleMeetingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingLinkRef",
                    "type": VehicleMeetingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRef",
                    "type": LineLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRef",
                    "type": WireLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRef",
                    "type": RoadLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRef",
                    "type": RailwayLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRef",
                    "type": ActivationLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    locating_system_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatingSystemRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
