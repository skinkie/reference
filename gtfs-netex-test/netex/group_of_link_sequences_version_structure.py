from dataclasses import dataclass, field
from typing import Optional
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .link_sequence_refs_rel_structure import LinkSequenceRefsRelStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinkSequencesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfLinkSequences_VersionStructure"

    members: Optional[LinkSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
