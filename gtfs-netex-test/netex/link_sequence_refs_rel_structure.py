from dataclasses import dataclass, field
from typing import List
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.dead_run_ref import DeadRunRef
from netex.journey_pattern_ref import JourneyPatternRef
from netex.link_sequence_ref import LinkSequenceRef
from netex.navigation_path_ref import NavigationPathRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.route_ref import RouteRef
from netex.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.service_journey_ref import ServiceJourneyRef
from netex.service_pattern_ref import ServicePatternRef
from netex.single_journey_path_ref import SingleJourneyPathRef
from netex.single_journey_ref import SingleJourneyRef
from netex.special_service_ref import SpecialServiceRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.timing_pattern_ref import TimingPatternRef
from netex.trip_pattern_trip_ref import TripPatternTripRef
from netex.trip_ref import TripRef
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkSequenceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of LINK SEQUENCEs.
    """
    class Meta:
        name = "linkSequenceRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
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
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
