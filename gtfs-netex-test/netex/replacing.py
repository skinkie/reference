from dataclasses import dataclass, field
from netex.replacing_version_structure import ReplacingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Replacing(ReplacingVersionStructure):
    """
    Whether the product can be replaced if lost or stolen.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
