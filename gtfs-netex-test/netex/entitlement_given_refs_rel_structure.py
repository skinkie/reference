from dataclasses import dataclass, field
from typing import List
from netex.entitlement_given_ref import EntitlementGivenRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementGivenRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for references to a ENTITLEMENT GIVEN PARAMETER.
    """
    class Meta:
        name = "entitlementGivenRefs_RelStructure"

    entitlement_given_ref: List[EntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
