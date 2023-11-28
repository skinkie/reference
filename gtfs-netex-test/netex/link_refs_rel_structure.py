from dataclasses import dataclass, field
from typing import List
from netex.activation_link_ref import ActivationLinkRef
from netex.activation_link_ref_by_value import ActivationLinkRefByValue
from netex.line_link_ref import LineLinkRef
from netex.line_link_ref_by_value import LineLinkRefByValue
from netex.link_ref_by_value import LinkRefByValue
from netex.modal_link_ref_by_value import ModalLinkRefByValue
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from netex.path_link_ref import PathLinkRef
from netex.path_link_ref_by_value import PathLinkRefByValue
from netex.railway_link_ref import RailwayLinkRef
from netex.railway_link_ref_by_value import RailwayLinkRefByValue
from netex.road_link_ref import RoadLinkRef
from netex.road_link_ref_by_value import RoadLinkRefByValue
from netex.route_link_ref import RouteLinkRef
from netex.route_link_ref_by_value import RouteLinkRefByValue
from netex.service_link_ref import ServiceLinkRef
from netex.service_link_ref_by_value import ServiceLinkRefByValue
from netex.timing_link_ref import TimingLinkRef
from netex.timing_link_ref_by_value import TimingLinkRefByValue
from netex.vehicle_meeting_link_ref import VehicleMeetingLinkRef
from netex.wire_link_ref import WireLinkRef
from netex.wire_link_ref_by_value import WireLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a LINK.
    """
    class Meta:
        name = "linkRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
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
                    "name": "ServiceLinkRefByValue",
                    "type": ServiceLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRefByValue",
                    "type": LineLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRefByValue",
                    "type": TimingLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRefByValue",
                    "type": WireLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRefByValue",
                    "type": RoadLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRefByValue",
                    "type": RailwayLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRefByValue",
                    "type": ActivationLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModalLinkRefByValue",
                    "type": ModalLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRefByValue",
                    "type": PathLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRefByValue",
                    "type": RouteLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkRefByValue",
                    "type": LinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
