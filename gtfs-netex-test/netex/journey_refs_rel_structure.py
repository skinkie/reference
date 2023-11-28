from dataclasses import dataclass, field
from typing import List
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.dead_run_ref import DeadRunRef
from netex.journey_designator import JourneyDesignator
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.service_designator import ServiceDesignator
from netex.service_journey_ref import ServiceJourneyRef
from netex.single_journey_ref import SingleJourneyRef
from netex.special_service_ref import SpecialServiceRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of JOURNEYs.
    """
    class Meta:
        name = "journeyRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "JourneyDesignator",
                    "type": JourneyDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceDesignator",
                    "type": ServiceDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
