from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF ACTIVATION.

    :ivar type_of_activation_ref: Reference to a TYPE OF ACTIVATION.
    """
    class Meta:
        name = "activationTypeRefs_RelStructure"

    type_of_activation_ref: List[TypeOfActivationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
