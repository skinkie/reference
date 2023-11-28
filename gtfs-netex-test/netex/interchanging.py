from dataclasses import dataclass, field
from netex.interchanging_version_structure import InterchangingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Interchanging(InterchangingVersionStructure):
    """
    Limitations on making changes within a trip.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
