from dataclasses import dataclass

from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinkSequence(LinkSequenceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
