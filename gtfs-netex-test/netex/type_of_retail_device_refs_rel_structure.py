from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_retail_device_ref import TypeOfRetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfRetailDeviceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF RETAIL DEVICE.
    """
    class Meta:
        name = "typeOfRetailDeviceRefs_RelStructure"

    type_of_retail_device_ref: List[TypeOfRetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
