from dataclasses import dataclass, field
from typing import List
from netex.activated_equipment import ActivatedEquipment
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivatedEquipmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ACTIVATION EQUIPMENTs.
    """
    class Meta:
        name = "activatedEquipmentsInFrame_RelStructure"

    activated_equipment: List[ActivatedEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ActivatedEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
