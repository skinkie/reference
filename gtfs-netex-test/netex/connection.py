from dataclasses import dataclass, field
from netex.connection_version_structure import ConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Connection(ConnectionVersionStructure):
    """The physical (spatial) possibility for a passenger to change from one public
    transport vehicle to another to continue the trip.

    Different times may be necessary to cover this link, depending on
    the kind of passenger.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
