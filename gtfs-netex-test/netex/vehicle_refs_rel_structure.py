from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleRefs_RelStructure"

    vehicle_ref: list[VehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
