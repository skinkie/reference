from dataclasses import dataclass

from .trailing_element_type_ref_structure import TrailingElementTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrailingElementTypeRef(TrailingElementTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
