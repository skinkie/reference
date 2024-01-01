from dataclasses import dataclass, field
from typing import List
from .activated_equipment import ActivatedEquipment
from .containment_aggregation_structure import ContainmentAggregationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activatedEquipmentsInFrame_RelStructure"

    activated_equipment: List[ActivatedEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ActivatedEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
