from dataclasses import dataclass, field
from netex.time_unit_version_structure import TimeUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeUnit(TimeUnitVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
