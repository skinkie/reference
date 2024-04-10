from dataclasses import dataclass, field

from .individual_traveller_ref import IndividualTravellerRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class IndividualTravellerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "individualTravellerRefs_RelStructure"

    individual_traveller_ref: IndividualTravellerRef = field(
        metadata={
            "name": "IndividualTravellerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
