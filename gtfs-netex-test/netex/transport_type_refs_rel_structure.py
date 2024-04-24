from dataclasses import dataclass, field
from typing import List, Union

from .compound_train_ref import CompoundTrainRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .powered_train_ref import PoweredTrainRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "transportTypeRefs_RelStructure"

    transport_type_ref_or_vehicle_type_ref_or_train_ref: List[Union[SimpleVehicleTypeRef, CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef, TransportTypeRef]] = field(
        default_factory=list,
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
