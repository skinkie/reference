from dataclasses import dataclass, field
from netex.wire_junction_version_structure import WireJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WireJunction(WireJunctionVersionStructure):
    """
    A type of INFRASTRUCTURE POINT used to describe a WIRE network.

    :ivar id: Identifier of WIRE JUNCTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
