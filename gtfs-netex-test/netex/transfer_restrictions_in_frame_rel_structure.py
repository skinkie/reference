from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .transfer_restriction import TransferRestriction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransferRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transferRestrictionsInFrame_RelStructure"

    transfer_restriction: list[TransferRestriction] = field(
        default_factory=list,
        metadata={
            "name": "TransferRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
