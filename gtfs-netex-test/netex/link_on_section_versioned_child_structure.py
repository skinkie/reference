from dataclasses import dataclass, field
from typing import Optional
from netex.activation_link import ActivationLink
from netex.activation_link_ref import ActivationLinkRef
from netex.line_link_ref import LineLinkRef
from netex.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from netex.path_link import PathLink
from netex.path_link_ref import PathLinkRef
from netex.railway_element import RailwayElement
from netex.railway_link_ref import RailwayLinkRef
from netex.road_element import RoadElement
from netex.road_link_ref import RoadLinkRef
from netex.route_link import RouteLink
from netex.route_link_ref import RouteLinkRef
from netex.service_link import ServiceLink
from netex.service_link_ref import ServiceLinkRef
from netex.site_path_link import SitePathLink
from netex.timing_link import TimingLink
from netex.timing_link_ref import TimingLinkRef
from netex.vehicle_meeting_link import VehicleMeetingLink
from netex.vehicle_meeting_link_ref import VehicleMeetingLinkRef
from netex.wire_element import WireElement
from netex.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkOnSectionVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    """Type for a LINK on a SECTION.

    +v1.1.

    :ivar choice_1:
    :ivar reverse: Whether link is navigated in to / from, i.e. reverse
        direction . Default is false, i.e. from to.
    """
    class Meta:
        name = "LinkOnSection_VersionedChildStructure"

    choice_1: Optional[object] = field(
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
                {
                    "name": "VehicleMeetingLink",
                    "type": VehicleMeetingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLink",
                    "type": ServiceLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLink",
                    "type": RouteLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLink",
                    "type": TimingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLink",
                    "type": ActivationLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
