from dataclasses import dataclass

from .type_of_proof_ref_structure import TypeOfProofRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfProofRef(TypeOfProofRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
