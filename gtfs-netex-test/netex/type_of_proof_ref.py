from dataclasses import dataclass
from netex.type_of_proof_ref_structure import TypeOfProofRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfProofRef(TypeOfProofRefStructure):
    """Reference to a TYPE OF PROOF.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
