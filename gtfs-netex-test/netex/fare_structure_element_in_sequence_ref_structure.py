from dataclasses import dataclass
from netex.fare_element_in_sequence_ref_structure import FareElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementInSequenceRefStructure(FareElementInSequenceRefStructure):
    """
    Type for Reference to a FARE STRUCTURE ELEMENT IN SEQUENCE.
    """
