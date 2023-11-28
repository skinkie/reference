from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.group_of_timebands import GroupOfTimebands

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimebandsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  GROUP OF TIME BANDs.
    """
    class Meta:
        name = "groupOfTimebandsInFrame_RelStructure"

    group_of_timebands: List[GroupOfTimebands] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
