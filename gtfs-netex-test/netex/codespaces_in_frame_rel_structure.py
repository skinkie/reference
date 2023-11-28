from dataclasses import dataclass, field
from typing import List
from netex.codespace import Codespace
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CODESPACEs.
    """
    class Meta:
        name = "codespacesInFrame_RelStructure"

    codespace: List[Codespace] = field(
        default_factory=list,
        metadata={
            "name": "Codespace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
