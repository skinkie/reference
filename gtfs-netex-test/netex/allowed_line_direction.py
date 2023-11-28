from dataclasses import dataclass, field
from netex.allowed_line_direction_version_structure import AllowedLineDirectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllowedLineDirection(AllowedLineDirectionVersionStructure):
    """
    A set of allowed DIRECTIONs that can be used on a given ROUTE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
