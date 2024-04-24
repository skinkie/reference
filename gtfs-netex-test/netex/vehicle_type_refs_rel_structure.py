from dataclasses import dataclass, field
from typing import List, Union

from .compound_train_ref import CompoundTrainRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .powered_train_ref import PoweredTrainRef
from .train_ref import TrainRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleTypeRefs_RelStructure"

    vehicle_type_ref_or_train_ref: List[Union[CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef]] = field(
        default_factory=list,
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
