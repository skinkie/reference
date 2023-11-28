from dataclasses import dataclass, field
from netex.communication_service_version_structure import CommunicationServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommunicationService(CommunicationServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to communication services.

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
