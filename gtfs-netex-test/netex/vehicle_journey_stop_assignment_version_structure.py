from dataclasses import dataclass, field
from typing import Optional, Union

from .dead_run_ref import DeadRunRef
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .passenger_stop_assignment_version_structure import PassengerStopAssignmentVersionStructure
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleJourneyStopAssignmentVersionStructure(PassengerStopAssignmentVersionStructure):
    class Meta:
        name = "VehicleJourneyStopAssignment_VersionStructure"

    vehicle_journey_ref: list[Union[DeadRunRef, VehicleJourneyRef]] = field(
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
        },
    )
    vehicle_journey_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[Union[DynamicStopAssignmentRef, VehicleJourneyStopAssignmentRef, PassengerStopAssignmentRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
