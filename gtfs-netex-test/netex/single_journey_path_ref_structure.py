from dataclasses import dataclass
from netex.link_sequence_ref_structure import LinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyPathRefStructure(LinkSequenceRefStructure):
    """
    Type for a reference to a SINGLE JOURNEY PATH.
    """
