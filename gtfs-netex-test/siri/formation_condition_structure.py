from dataclasses import dataclass, field
from typing import Optional, Union

from .compound_train_ref import CompoundTrainRef
from .entrance_to_vehicle_ref import EntranceToVehicleRef
from .extensions_1 import Extensions1
from .formation_status_structure import FormationStatusStructure
from .recommended_action_structure import RecommendedActionStructure
from .situation_ref import SituationRef
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_ref import TrainRef
from .vehicle_in_formation_status_structure import VehicleInFormationStatusStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FormationConditionStructure:
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
    formation_status_or_vehicle_in_formation_status: Optional[Union[FormationStatusStructure, VehicleInFormationStatusStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FormationStatus",
                    "type": FormationStatusStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "VehicleInFormationStatus",
                    "type": VehicleInFormationStatusStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recommended_action: Optional[RecommendedActionStructure] = field(
        default=None,
        metadata={
            "name": "RecommendedAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
