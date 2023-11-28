from dataclasses import dataclass, field
from typing import Optional
from netex.call_versioned_child_structure import CallVersionedChildStructure
from netex.estimated_passing_time_view import EstimatedPassingTimeView
from netex.observed_passing_time_view import ObservedPassingTimeView
from netex.onward_calls_rel_structure import OnwardCallsRelStructure
from netex.previous_calls_rel_structure import PreviousCallsRelStructure
from netex.target_passing_time_view import TargetPassingTimeView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonitoredCallVersionedChildStructure(CallVersionedChildStructure):
    """
    Data type for Monitored CALL.

    :ivar target_passing_time_view:
    :ivar estimated_passing_time_view:
    :ivar observed_passing_time_view:
    :ivar previous_calls: Previous stops  in the SERVICE PATTERN.
    :ivar onward_calls: Onwards stops  in the SERVICE PATTERN.
    """
    class Meta:
        name = "MonitoredCall_VersionedChildStructure"

    target_passing_time_view: Optional[TargetPassingTimeView] = field(
        default=None,
        metadata={
            "name": "TargetPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    estimated_passing_time_view: Optional[EstimatedPassingTimeView] = field(
        default=None,
        metadata={
            "name": "EstimatedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    observed_passing_time_view: Optional[ObservedPassingTimeView] = field(
        default=None,
        metadata={
            "name": "ObservedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    previous_calls: Optional[PreviousCallsRelStructure] = field(
        default=None,
        metadata={
            "name": "previousCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_calls: Optional[OnwardCallsRelStructure] = field(
        default=None,
        metadata={
            "name": "onwardCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
