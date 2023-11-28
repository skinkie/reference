from dataclasses import dataclass, field
from typing import Optional
from netex.data_managed_object_view_structure import DataManagedObjectViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassingTimeViewStructure(DataManagedObjectViewStructure):
    """
    Type for Simplified  TARGET PASSING TIME.

    :ivar day_offset: Number of days after the starting departure time
        of the journey if  not same calendar day. Default is 0 for same
        day.
    """
    class Meta:
        name = "PassingTime_ViewStructure"

    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
