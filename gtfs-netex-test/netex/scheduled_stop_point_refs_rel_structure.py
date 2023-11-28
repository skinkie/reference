from dataclasses import dataclass, field
from typing import Optional
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of SCHEDULED STOP POINTs.
    """
    class Meta:
        name = "scheduledStopPointRefs_RelStructure"

    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
