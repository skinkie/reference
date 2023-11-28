from dataclasses import dataclass, field
from typing import List
from netex.authority_ref import AuthorityRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.operator_ref import OperatorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportOrganisationRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to an OPERATOR.
    """
    class Meta:
        name = "transportOrganisationRefs_RelStructure"

    authority_ref_or_operator_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
