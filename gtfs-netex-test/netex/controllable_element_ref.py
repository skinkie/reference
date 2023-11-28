from dataclasses import dataclass
from netex.controllable_element_ref_structure import ControllableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementRef(ControllableElementRefStructure):
    """
    Reference to a CONTROLLABLE ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
