from dataclasses import dataclass, field
from typing import List, Optional, Union

from .compound_train_ref import CompoundTrainRef
from .entrance_to_vehicle_ref import EntranceToVehicleRef
from .stop_assignment_structure import StopAssignmentStructure
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_ref import TrainRef
from .vehicle_in_formation_status_structure import VehicleInFormationStatusStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FormationAssignmentStructure:
    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_ref_or_train_in_compound_train_ref: Optional[Union[TrainRef, TrainInCompoundTrainRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TrainInCompoundTrainRef",
                    "type": TrainInCompoundTrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    train_element_ref_or_train_component_ref: Optional[Union[TrainElementRef, TrainComponentRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    entrance_to_vehicle_ref: Optional[EntranceToVehicleRef] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_in_formation_status: Optional[VehicleInFormationStatusStructure] = field(
        default=None,
        metadata={
            "name": "VehicleInFormationStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_stop_assignment: List[StopAssignmentStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
