from dataclasses import dataclass
from .layer_version_structure import LayerVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Layer(LayerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
