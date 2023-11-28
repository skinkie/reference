from dataclasses import dataclass, field
from netex.retail_service_version_structure import RetailServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailService(RetailServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to retail services.

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
