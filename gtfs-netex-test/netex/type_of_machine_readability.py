from dataclasses import dataclass, field
from netex.type_of_machine_readability_version_structure import TypeOfMachineReadabilityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMachineReadability(TypeOfMachineReadabilityVersionStructure):
    """
    A classification of MACHINE REDABILITY capabailities, used for example to
    indicate how a TRAVEL DOCUMENT may be read.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
