from dataclasses import dataclass

from .fare_element_in_sequence_ref_structure import FareElementInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareStructureElementInSequenceRefStructure(FareElementInSequenceRefStructure):
    pass
