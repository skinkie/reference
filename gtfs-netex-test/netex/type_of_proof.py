from dataclasses import dataclass, field
from netex.type_of_proof_value_structure import TypeOfProofValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfProof(TypeOfProofValueStructure):
    """Type of Proff of identity required.

    +v1.2.2

    :ivar id: Identifier of TYPE OF PROOF .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
