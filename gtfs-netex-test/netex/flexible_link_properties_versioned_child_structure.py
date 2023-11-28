from dataclasses import dataclass, field
from typing import Optional
from netex.activation_link_ref import ActivationLinkRef
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.flexible_link_type_enumeration import FlexibleLinkTypeEnumeration
from netex.line_link_ref import LineLinkRef
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
class FlexibleLinkPropertiesVersionedChildStructure(VersionedChildStructure):
    """
    Type for FLEXIBLE LINK PROPERTies.

    :ivar choice:
    :ivar may_be_skipped: Whether the LINK may be skipped.
    :ivar on_main_route: Whether the LINK is on the main ROUTE of the
        LINE.
    :ivar unscheduled_path: Whether this link is on an unscheduled path
        route.
    :ivar flexible_link_type: Type of flexible link.
    """
    class Meta:
        name = "FlexibleLinkProperties_VersionedChildStructure"

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
    unscheduled_path: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnscheduledPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_link_type: Optional[FlexibleLinkTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleLinkType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
