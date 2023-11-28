from dataclasses import dataclass
from netex.controllable_element_in_sequence_ref_structure import ControllableElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementInSequenceRef(ControllableElementInSequenceRefStructure):
    """
    Reference to an CONTROLLABLE ELEMENT IN SEQUENCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
