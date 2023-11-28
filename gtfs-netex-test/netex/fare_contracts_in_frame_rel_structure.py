from dataclasses import dataclass, field
from typing import List
from netex.fare_contract import FareContract
from netex.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of SALES FARE CONTRACTs.
    """
    class Meta:
        name = "fareContractsInFrame_RelStructure"

    fare_contract: List[FareContract] = field(
        default_factory=list,
        metadata={
            "name": "FareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
