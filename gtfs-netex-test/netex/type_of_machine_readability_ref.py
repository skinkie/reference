from dataclasses import dataclass
from netex.type_of_machine_readability_ref_structure import TypeOfMachineReadabilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMachineReadabilityRef(TypeOfMachineReadabilityRefStructure):
    """
    Reference to a TYPE OF MACHINE READABILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
