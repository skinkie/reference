from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .tariff import Tariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TariffsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "tariffsInFrame_RelStructure"

    tariff: list[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
