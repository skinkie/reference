from dataclasses import dataclass
from netex.type_of_mode_of_operation_ref_structure import TypeOfModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfModeOfOperationRef(TypeOfModeOfOperationRefStructure):
    """
    Reference to a TYPE OF MODE OF OPERATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
