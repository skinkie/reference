from dataclasses import dataclass, field
from typing import Optional, Union

from .activation_link import ActivationLink
from .activation_link_ref import ActivationLinkRef
from .deck_path_link import DeckPathLink
from .deck_path_link_ref import DeckPathLinkRef
from .generic_path_link import GenericPathLink
from .generic_path_link_ref import GenericPathLinkRef
from .line_link_ref import LineLinkRef
from .link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from .off_site_path_link import OffSitePathLink
from .off_site_path_link_ref import OffSitePathLinkRef
from .onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from .path_link import PathLink
from .path_link_ref import PathLinkRef
from .railway_element import RailwayElement
from .railway_link_ref import RailwayLinkRef
from .road_element import RoadElement
from .road_link_ref import RoadLinkRef
from .route_link import RouteLink
from .route_link_ref import RouteLinkRef
from .service_link import ServiceLink
from .service_link_ref import ServiceLinkRef
from .site_path_link import SitePathLink
from .site_path_link_ref import SitePathLinkRef
from .timing_link import TimingLink
from .timing_link_ref import TimingLinkRef
from .vehicle_meeting_link import VehicleMeetingLink
from .vehicle_meeting_link_ref import VehicleMeetingLinkRef
from .wire_element import WireElement
from .wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinkOnSectionVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "LinkOnSection_VersionedChildStructure"

    link_ref_or_infrastructure_link_ref_or_generic_path_link_ref_or_link_or_infrastructure_link: Optional[
        Union[
            OnwardVehicleMeetingLinkRef,
            VehicleMeetingLinkRef,
            ServiceLinkRef,
            LineLinkRef,
            TimingLinkRef,
            WireLinkRef,
            RoadLinkRef,
            RailwayLinkRef,
            ActivationLinkRef,
            RouteLinkRef,
            DeckPathLinkRef,
            OffSitePathLinkRef,
            PathLinkRef,
            SitePathLinkRef,
            GenericPathLinkRef,
            VehicleMeetingLink,
            ServiceLink,
            RouteLink,
            TimingLink,
            WireElement,
            RoadElement,
            RailwayElement,
            ActivationLink,
            DeckPathLink,
            PathLink,
            SitePathLink,
            OffSitePathLink,
            GenericPathLink,
        ]
    ] = field(
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
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckPathLinkRef",
                    "type": DeckPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffSitePathLinkRef",
                    "type": OffSitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLinkRef",
                    "type": SitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathLinkRef",
                    "type": GenericPathLinkRef,
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
                {
                    "name": "DeckPathLink",
                    "type": DeckPathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffSitePathLink",
                    "type": OffSitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathLink",
                    "type": GenericPathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
