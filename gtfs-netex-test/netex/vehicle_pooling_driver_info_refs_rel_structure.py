from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingDriverInfoRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE POOLING DRIVER INFOs.
    """
    class Meta:
        name = "vehiclePoolingDriverInfoRefs_RelStructure"

    vehicle_pooling_driver_info_ref: VehiclePoolingDriverInfoRef = field(
        metadata={
            "name": "VehiclePoolingDriverInfoRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
