from dataclasses import dataclass, field
from netex.fleet_version_structure import FleetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Fleet(FleetVersionStructure):
    """A set of vehicles of any type.

    +v1.2.2

    :ivar id: Identifier of FLEET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
