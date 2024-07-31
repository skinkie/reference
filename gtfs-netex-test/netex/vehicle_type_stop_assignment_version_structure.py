from dataclasses import dataclass, field
from typing import Optional, Union

from .compound_train_ref import CompoundTrainRef
from .dead_run_ref import DeadRunRef
from .powered_train_ref import PoweredTrainRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_orientation_enumeration import VehicleOrientationEnumeration
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "VehicleTypeStopAssignment_VersionStructure"

    vehicle_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journey_ref: Optional[Union[DeadRunRef, VehicleJourneyRef]] = field(
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
