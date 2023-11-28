from dataclasses import dataclass, field
from netex.transport_type_version_structure import TransportTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportType(TransportTypeVersionStructure):
    """
    A classification of any type of VEHICLE according to its properties.

    :ivar id: Identifier of TRANSPORT TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
