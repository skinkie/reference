from dataclasses import dataclass

from .passenger_at_stop_time_versioned_child_structure import PassengerAtStopTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerAtStopTime(PassengerAtStopTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
