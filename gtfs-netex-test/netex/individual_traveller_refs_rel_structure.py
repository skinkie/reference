from dataclasses import dataclass, field
from netex.individual_traveller_ref import IndividualTravellerRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualTravellerRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of INDIVIDUAL TRAVELLERs.
    """
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
