from dataclasses import dataclass, field
from netex.quay_version_structure import QuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Quay(QuayVersionStructure):
    """A place such as platform, stance, or quayside where passengers have access
    to PT vehicles, Taxi cars or other means of transportation.

    A QUAY may contain other sub QUAYs. A child QUAY must be physically
    contained within its parent QUAY.

    :ivar id: Identifier of QUAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
