from dataclasses import dataclass

from .tractive_element_type_ref_structure import TractiveElementTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TractiveElementTypeRef(TractiveElementTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
