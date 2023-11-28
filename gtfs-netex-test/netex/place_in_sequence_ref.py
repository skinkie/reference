from dataclasses import dataclass
from netex.place_in_sequence_ref_structure import PlaceInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceInSequenceRef(PlaceInSequenceRefStructure):
    """Reference to a PLACE IN SEQUENCE.

    If given by context does not need to be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
