from dataclasses import dataclass
from netex.fare_structure_element_ref_structure import FareStructureElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementRef(FareStructureElementRefStructure):
    """
    Reference to a FARE STRUCTURE ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
