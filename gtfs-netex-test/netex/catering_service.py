from dataclasses import dataclass, field
from netex.catering_service_version_structure import CateringServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CateringService(CateringServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to catering service.

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
