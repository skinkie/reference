from dataclasses import dataclass
from netex.fare_structure_element_in_sequence_versioned_child_structure import FareStructureElementInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementInSequence(FareStructureElementInSequenceVersionedChildStructure):
    """
    A FARE STRUCTURE ELEMENT as a part of a VALIDABLE ELEMENT, including its
    possible order in the sequence of FARE STRUCTURE ELEMENTs forming that
    VALIDABLE ELEMENT, and its possible quantitative limitation.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
