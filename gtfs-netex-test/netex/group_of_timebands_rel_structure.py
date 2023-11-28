from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.group_of_timebands_ref import GroupOfTimebandsRef
from netex.group_of_timebands_versioned_child_structure import GroupOfTimebandsVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimebandsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of GROUP OF TIMEBANDS.
    """
    class Meta:
        name = "groupOfTimebands_RelStructure"

    group_of_timebands_ref_or_group_of_timebands: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfTimebandsRef",
                    "type": GroupOfTimebandsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebands",
                    "type": GroupOfTimebandsVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
