from dataclasses import dataclass, field
from netex.stop_area_version_structure import StopAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopArea(StopAreaVersionStructure):
    """
    A group of STOP POINTs close to each other.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
