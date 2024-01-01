from dataclasses import dataclass
from .group_of_link_sequences_version_structure import (
    GroupOfLinkSequencesVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinkSequences(GroupOfLinkSequencesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
