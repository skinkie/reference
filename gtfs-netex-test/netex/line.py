from dataclasses import dataclass, field
from netex.line_version_structure import LineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Line(LineVersionStructure):
    """
    A group of ROUTEs which is generally known to the public by a similar name or
    number.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
