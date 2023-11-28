from dataclasses import dataclass, field
from netex.access_space_version_structure import AccessSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessSpace(AccessSpaceVersionStructure):
    """An area within a STOP PLACE that does not give direct access to transport
    vehicles.

    May be connected to QUAYS by PATH LINKs.

    :ivar id: Identifier of ACCESS SPACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
