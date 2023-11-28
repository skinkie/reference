from dataclasses import dataclass, field
from netex.relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReliefPoint(ReliefPointVersionStructure):
    """A TIMING POINT where a relief is possible, i.e. a driver may take on or hand
    over a vehicle.

    The vehicle may sometimes be left unattended.

    :ivar id: Identifier of  a RELIEF POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
