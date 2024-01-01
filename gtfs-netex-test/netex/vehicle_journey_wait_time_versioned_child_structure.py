from dataclasses import dataclass, field
from typing import Optional, Union
from .dead_run_ref import DeadRunRef
from .journey_wait_time_versioned_child_structure import (
    JourneyWaitTimeVersionedChildStructure,
)
from .vehicle_journey_ref import VehicleJourneyRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyWaitTimeVersionedChildStructure(
    JourneyWaitTimeVersionedChildStructure
):
    class Meta:
        name = "VehicleJourneyWaitTime_VersionedChildStructure"

    vehicle_journey_ref: Optional[
        Union[DeadRunRef, VehicleJourneyRef]
    ] = field(
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
        },
    )
