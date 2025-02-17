from dataclasses import dataclass

from .link_sequence_ref_structure import LinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinkSequenceRef(LinkSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
