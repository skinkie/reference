from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .compound_train_ref import CompoundTrainRef
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .entity_in_version_structure import VersionedChildStructure
from .fare_point_in_pattern_ref import FarePointInPatternRef
from .multilingual_string import MultilingualString
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef
from .point_in_journey_pattern_ref import PointInJourneyPatternRef
from .point_in_single_journey_path_ref import PointInSingleJourneyPathRef
from .powered_train_ref import PoweredTrainRef
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .timing_point_in_journey_pattern_ref import TimingPointInJourneyPatternRef
from .train_ref import TrainRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_ref import VehicleRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingStepVersionStructure(VersionedChildStructure):
    class Meta:
        name = "RechargingStep_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charge_energy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChargeEnergy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    target_energy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TargetEnergy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ChargingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    finalisation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinalisationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    point_in_journey_pattern_ref: Optional[Union[PointInSingleJourneyPathRef, FarePointInPatternRef, StopPointInJourneyPatternRef, TimingPointInJourneyPatternRef, PointInJourneyPatternRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointInSingleJourneyPathRef",
                    "type": PointInSingleJourneyPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPatternRef",
                    "type": StopPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPatternRef",
                    "type": TimingPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_type_ref_or_train_ref: Optional[Union[CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
