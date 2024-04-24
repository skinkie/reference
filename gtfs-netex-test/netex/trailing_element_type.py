from dataclasses import dataclass

from .trailing_element_type_version_structure import TrailingElementTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrailingElementType(TrailingElementTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
