from dataclasses import dataclass, field
from typing import List
from netex.dead_run_ref import DeadRunRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE JOURNEYs.
    """
    class Meta:
        name = "vehicleJourneyRefs_RelStructure"

    dead_run_ref_or_vehicle_journey_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
