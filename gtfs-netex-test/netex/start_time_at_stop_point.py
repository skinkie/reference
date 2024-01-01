from dataclasses import dataclass
from .start_time_at_stop_point_versioned_child_structure import (
    StartTimeAtStopPointVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StartTimeAtStopPoint(StartTimeAtStopPointVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
