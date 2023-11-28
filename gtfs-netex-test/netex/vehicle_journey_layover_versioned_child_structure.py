from dataclasses import dataclass, field
from typing import Optional
from netex.dead_run_ref import DeadRunRef
from netex.journey_layover_structure import JourneyLayoverStructure
from netex.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyLayoverVersionedChildStructure(JourneyLayoverStructure):
    """
    Type for a VEHICLE JOURNEY LAYOVER.
    """
    class Meta:
        name = "VehicleJourneyLayover_VersionedChildStructure"

    dead_run_ref_or_vehicle_journey_ref: Optional[object] = field(
        default=None,
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
