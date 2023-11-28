from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.tariff import Tariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TariffsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TARIFF.
    """
    class Meta:
        name = "tariffsInFrame_RelStructure"

    tariff: List[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
