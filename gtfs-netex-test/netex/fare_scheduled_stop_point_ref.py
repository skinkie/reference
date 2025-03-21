from dataclasses import dataclass

from .fare_scheduled_stop_point_ref_structure import FareScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareScheduledStopPointRef(FareScheduledStopPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
