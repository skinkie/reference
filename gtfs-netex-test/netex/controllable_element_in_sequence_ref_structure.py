from dataclasses import dataclass
from netex.fare_element_in_sequence_ref_structure import FareElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementInSequenceRefStructure(FareElementInSequenceRefStructure):
    """
    Type for Reference to an CONTROLLABLE ELEMENT IN SEQUENCE.
    """
