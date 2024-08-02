from dataclasses import dataclass, field
from typing import Any

from .train_component_stop_assignment_version_structure import TrainComponentStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentStopAssignment(TrainComponentStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    vehicle_journey_stop_assignment_ref_or_passenger_stop_assignment_ref_1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    train_ref_1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    train_component_ref_or_train_component_view: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    position_of_train_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    boarding_position_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    is_allowed: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    entrance_to_vehicle: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    deck_entrance_assignments: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    boarding_use: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alighting_use: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    private_code: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    arrives_forwards: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    departs_forwards: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    arrives_from_left: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    departs_to_right: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
