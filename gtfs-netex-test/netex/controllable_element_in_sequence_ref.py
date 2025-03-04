from dataclasses import dataclass

from .controllable_element_in_sequence_ref_structure import ControllableElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ControllableElementInSequenceRef(ControllableElementInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
