from dataclasses import dataclass

from .fare_structure_element_in_sequence_ref_structure import FareStructureElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementInSequenceRef(FareStructureElementInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
