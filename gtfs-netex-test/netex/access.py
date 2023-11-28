from dataclasses import dataclass, field
from netex.access_version_structure import AccessVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Access(AccessVersionStructure):
    """The physical (spatial) possibility for a passenger to access or leave the
    public transport system.

    This link may be used during a trip for:- the walking movement of a
    passenger from a PLACE (origin of the trip) to a STOP POINT (origin
    of the PT TRIP), or- the walking movement from a STOP POINT
    (destination of the PT TRIP) to a PLACE (destination of the trip).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
