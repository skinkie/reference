from dataclasses import dataclass, field

from .occupancy_enumeration import OccupancyEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Occupancy:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: OccupancyEnumeration = field(
        metadata={
            "required": True,
        }
    )
