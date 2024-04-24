from dataclasses import dataclass

from .passenger_at_stop_time_ref_structure import PassengerAtStopTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerAtStopTimeRef(PassengerAtStopTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
