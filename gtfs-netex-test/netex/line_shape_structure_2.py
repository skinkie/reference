from dataclasses import dataclass, field
from typing import Optional, Union

from .activation_link_ref import ActivationLinkRef
from .deck_path_link_ref import DeckPathLinkRef
from .entity_in_version_structure import DataManagedObjectStructure
from .generic_path_link_ref import GenericPathLinkRef
from .line_link_ref import LineLinkRef
from .multilingual_string import MultilingualString
from .off_site_path_link_ref import OffSitePathLinkRef
from .onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from .path_link_ref import PathLinkRef
from .railway_link_ref import RailwayLinkRef
from .road_link_ref import RoadLinkRef
from .route_link_ref import RouteLinkRef
from .service_link_ref import ServiceLinkRef
from .site_path_link_ref import SitePathLinkRef
from .timing_link_ref import TimingLinkRef
from .vehicle_meeting_link_ref import VehicleMeetingLinkRef
from .wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LineShapeStructure2(DataManagedObjectStructure):
    class Meta:
        name = "LineShapeStructure"

    formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "Formula",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_ref_or_infrastructure_link_ref_or_generic_path_link_ref: Optional[
        Union[OnwardVehicleMeetingLinkRef, VehicleMeetingLinkRef, ServiceLinkRef, LineLinkRef, TimingLinkRef, WireLinkRef, RoadLinkRef, RailwayLinkRef, ActivationLinkRef, RouteLinkRef, DeckPathLinkRef, OffSitePathLinkRef, PathLinkRef, SitePathLinkRef, GenericPathLinkRef]
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
            ),
        },
    )
    locating_system_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatingSystemRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
