from dataclasses import dataclass, field
from typing import List

from .group_of_services_ref import GroupOfServicesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfServicesRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupOfServicesRefs_RelStructure"

    group_of_services_ref: List[GroupOfServicesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
