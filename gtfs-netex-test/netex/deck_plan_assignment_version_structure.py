from dataclasses import dataclass, field
from typing import Optional, Union

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .compound_train_ref import CompoundTrainRef
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .deck_plan_ref import DeckPlanRef
from .journey_part_ref import JourneyPartRef
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef
from .powered_train_ref import PoweredTrainRef
from .service_journey_ref import ServiceJourneyRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .tractive_element_type_ref import TractiveElementTypeRef
from .trailing_element_type_ref import TrailingElementTypeRef
from .train_component_ref import TrainComponentRef
from .train_element_type_ref import TrainElementTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .unpowered_train_ref import UnpoweredTrainRef
from .validity_condition_refs_rel_structure import ValidityConditionRefsRelStructure
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "DeckPlanAssignment_VersionStructure"

    deck_plan_ref: DeckPlanRef = field(
        metadata={
            "name": "DeckPlanRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_type_ref_or_vehicle_type_ref_or_train_ref: Optional[Union[SimpleVehicleTypeRef, CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef, TransportTypeRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UnpoweredTrainRef",
                    "type": UnpoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoweredTrainRef",
                    "type": PoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_type_ref: Optional[Union[TrailingElementTypeRef, TractiveElementTypeRef, TrainElementTypeRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrailingElementTypeRef",
                    "type": TrailingElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveElementTypeRef",
                    "type": TractiveElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementTypeRef",
                    "type": TrainElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    journey_ref_or_special_service_ref_or_service_journey_ref_or_vehicle_journey_ref: Optional[Union[SingleJourneyRef, NormalDatedVehicleJourneyRef, DatedVehicleJourneyRef, DatedSpecialServiceRef, SpecialServiceRef, TemplateServiceJourneyRef, ServiceJourneyRef, DeadRunRef, VehicleJourneyRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourneyRef",
                    "type": NormalDatedVehicleJourneyRef,
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
            ),
        },
    )
    journey_part_ref: Optional[JourneyPartRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    configuration_conditions: Optional[ValidityConditionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "configurationConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
