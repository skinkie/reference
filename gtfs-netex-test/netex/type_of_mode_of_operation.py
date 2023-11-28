from dataclasses import dataclass, field
from netex.type_of_mode_of_operation_value_structure import TypeOfModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfModeOfOperation(TypeOfModeOfOperationValueStructure):
    """A classification for a MODE OF OPERATION.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
