from dataclasses import dataclass, field
from netex.type_of_service_structure import TypeOfServiceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfService(TypeOfServiceStructure):
    """
    Classification of a Service.

    :ivar id: Reference to a TYPE OF SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
