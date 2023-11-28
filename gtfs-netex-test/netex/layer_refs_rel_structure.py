from dataclasses import dataclass, field
from typing import List
from netex.layer_ref import LayerRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LayerRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a LAYER.
    """
    class Meta:
        name = "layerRefs_RelStructure"

    layer_ref: List[LayerRef] = field(
        default_factory=list,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
