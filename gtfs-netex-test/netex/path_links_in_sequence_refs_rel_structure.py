from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .path_link_in_sequence_ref import PathLinkInSequenceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinksInSequenceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "pathLinksInSequenceRefs_RelStructure"

    path_link_in_sequence_ref: List[PathLinkInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
