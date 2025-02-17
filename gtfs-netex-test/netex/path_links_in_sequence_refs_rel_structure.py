from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .path_link_in_sequence_ref import PathLinkInSequenceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PathLinksInSequenceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "pathLinksInSequenceRefs_RelStructure"

    path_link_in_sequence_ref: list[PathLinkInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
