from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_organisation_ref import TypeOfOrganisationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfOrganisationRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF ORGANISATION.
    """
    class Meta:
        name = "typeOfOrganisationRefs_RelStructure"

    type_of_organisation_ref: List[TypeOfOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
