from dataclasses import dataclass, field
from typing import Optional
from netex.type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMediumAccessDeviceValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF MEDIUM ACCESS DEVICE.
    """
    class Meta:
        name = "TypeOfMediumAccessDevice_ValueStructure"

    type_of_machine_readability_ref: Optional[TypeOfMachineReadabilityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
