from dataclasses import dataclass
from netex.validable_element_ref_structure import ValidableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidableElementRef(ValidableElementRefStructure):
    """
    Reference to a VALIDABLE ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
