from dataclasses import dataclass, field
from netex.heading_sign_structure import HeadingSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HeadingSign(HeadingSignStructure):
    """
    Specialisation of SIGN EQUIPMENT for headings providing information like
    direction name, line name, etc.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
