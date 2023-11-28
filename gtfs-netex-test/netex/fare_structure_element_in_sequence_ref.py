from dataclasses import dataclass
from netex.fare_structure_element_in_sequence_ref_structure import FareStructureElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementInSequenceRef(FareStructureElementInSequenceRefStructure):
    """
    Reference to a FARE STRUCTURE ELEMENT IN SEQUENCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
