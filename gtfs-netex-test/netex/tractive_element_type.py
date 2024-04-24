from dataclasses import dataclass

from .tractive_element_type_version_structure import TractiveElementTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TractiveElementType(TractiveElementTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
