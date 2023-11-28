from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.transfer_restriction import TransferRestriction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TRANSFER RESTRICTION.

    :ivar transfer_restriction: A CONSTRAINT that can be applied on a
        CONNECTION or INTERCHANGE between two SCHEDULED STOP POINT,
        preventing or forbidding the passenger to use it.
    """
    class Meta:
        name = "transferRestrictionsInFrame_RelStructure"

    transfer_restriction: List[TransferRestriction] = field(
        default_factory=list,
        metadata={
            "name": "TransferRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
