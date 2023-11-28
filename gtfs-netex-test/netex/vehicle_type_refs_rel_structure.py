from dataclasses import dataclass, field
from typing import List
from netex.compound_train_ref import CompoundTrainRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.train_ref import TrainRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE TYPEs.
    """
    class Meta:
        name = "vehicleTypeRefs_RelStructure"

    compound_train_ref_or_train_ref_or_vehicle_type_ref: List[object] = field(
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
        }
    )
