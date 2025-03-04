from dataclasses import dataclass

from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Journey2(LinkSequenceVersionStructure):
    class Meta:
        name = "Journey_"
        namespace = "http://www.netex.org.uk/netex"
