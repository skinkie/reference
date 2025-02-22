from dataclasses import dataclass

from .layer_ref_structure import LayerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LayerRef(LayerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
