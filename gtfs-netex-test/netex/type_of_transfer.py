from dataclasses import dataclass, field
from netex.type_of_transfer_value_structure import TypeOfTransferValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTransfer(TypeOfTransferValueStructure):
    """
    Classification of a TRANSFER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
