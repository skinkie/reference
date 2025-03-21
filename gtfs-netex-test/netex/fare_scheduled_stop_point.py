from dataclasses import dataclass

from .fare_scheduled_stop_point_version_structure import FareScheduledStopPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareScheduledStopPoint(FareScheduledStopPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
