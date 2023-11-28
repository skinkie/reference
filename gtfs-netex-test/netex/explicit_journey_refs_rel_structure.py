from dataclasses import dataclass, field
from typing import List
from netex.dead_run_ref import DeadRunRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.service_journey_ref import ServiceJourneyRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExplicitJourneyRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of JOURNEYs.
    """
    class Meta:
        name = "explicitJourneyRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
