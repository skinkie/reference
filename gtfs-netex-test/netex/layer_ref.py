from dataclasses import dataclass
from netex.layer_ref_structure import LayerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LayerRef(LayerRefStructure):
    """
    Reference to a LAYER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
