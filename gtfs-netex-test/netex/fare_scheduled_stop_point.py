from dataclasses import dataclass, field
from netex.fare_scheduled_stop_point_version_structure import FareScheduledStopPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareScheduledStopPoint(FareScheduledStopPointVersionStructure):
    """
    A POINT where passengers can board or alight from vehicles.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
