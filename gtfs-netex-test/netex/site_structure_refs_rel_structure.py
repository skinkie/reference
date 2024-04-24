from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .site_structure_ref import SiteStructureRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteStructureRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "siteStructureRefs_RelStructure"

    site_structure_ref: List[SiteStructureRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteStructureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
