from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationalUnitRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of ORGANISATIONAL UNITs.
    """
    class Meta:
        name = "organisationalUnitRefs_RelStructure"

    organisational_unit_ref: List[OrganisationalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
