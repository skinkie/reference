from dataclasses import dataclass, field
from typing import List
from netex.compound_train_ref import CompoundTrainRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.train_ref import TrainRef
from netex.transport_type_ref import TransportTypeRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TRANSPORT TYPEs.
    """
    class Meta:
        name = "transportTypeRefs_RelStructure"

    choice: List[object] = field(
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
        }
    )
