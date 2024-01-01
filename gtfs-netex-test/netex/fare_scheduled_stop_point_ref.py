from dataclasses import dataclass
from .fare_scheduled_stop_point_ref_structure import (
    FareScheduledStopPointRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareScheduledStopPointRef(FareScheduledStopPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
