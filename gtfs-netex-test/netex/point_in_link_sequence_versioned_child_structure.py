from dataclasses import dataclass, field
from typing import Optional, Union

from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dead_run_ref import DeadRunRef
from .deck_navigation_path_ref import DeckNavigationPathRef
from .entity_in_version_structure import VersionedChildStructure
from .generic_navigation_path_ref import GenericNavigationPathRef
from .journey_pattern_ref import JourneyPatternRef
from .link_sequence_ref import LinkSequenceRef
from .multilingual_string import MultilingualString
from .navigation_path_ref import NavigationPathRef
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef
from .projections_rel_structure import ProjectionsRelStructure
from .route_ref import RouteRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
from .service_pattern_ref import ServicePatternRef
from .single_journey_path_ref import SingleJourneyPathRef
from .single_journey_ref import SingleJourneyRef
from .site_navigation_path_ref import SiteNavigationPathRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .timing_pattern_ref import TimingPatternRef
from .trip_pattern_trip_ref import TripPatternTripRef
from .trip_ref import TripRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointInLinkSequenceVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "PointInLinkSequence_VersionedChildStructure"

    link_sequence_ref_or_journey_ref_or_special_service_ref_or_service_journey_ref_or_vehicle_journey_ref_or_journey_pattern_ref_or_generic_navigation_path_ref: Optional[
        Union[
            TripRef,
            TripPatternTripRef,
            SingleJourneyPathRef,
            SingleJourneyRef,
            NormalDatedVehicleJourneyRef,
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            TimingPatternRef,
            RouteRef,
            DeckNavigationPathRef,
            NavigationPathRef,
            SiteNavigationPathRef,
            GenericNavigationPathRef,
            LinkSequenceRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TripRef",
                    "type": TripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripPatternTripRef",
                    "type": TripPatternTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourneyPathRef",
                    "type": SingleJourneyPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourneyRef",
                    "type": NormalDatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPatternRef",
                    "type": TimingPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckNavigationPathRef",
                    "type": DeckNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteNavigationPathRef",
                    "type": SiteNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericNavigationPathRef",
                    "type": GenericNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
