from dataclasses import dataclass, field
from typing import Optional, Union

from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .journey_pattern_ref import JourneyPatternRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .vehicle_journey_stop_assignment_version_structure import VehicleJourneyStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignmentVersionStructure(VehicleJourneyStopAssignmentVersionStructure):
    class Meta:
        name = "DynamicStopAssignment_VersionStructure"

    journey_pattern_ref: Optional[Union[ServiceJourneyPatternRef, ServicePatternRef, DeadRunJourneyPatternRef, JourneyPatternRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
