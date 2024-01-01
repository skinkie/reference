from dataclasses import dataclass
from .layer_ref_structure import LayerRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LayerRef(LayerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
