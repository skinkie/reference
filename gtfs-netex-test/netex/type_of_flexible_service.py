from dataclasses import dataclass, field
from netex.type_of_flexible_service_value_structure import TypeOfFlexibleServiceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFlexibleService(TypeOfFlexibleServiceValueStructure):
    """
    A classification of FLEXIBLE SERVICEs according to their functional purpose.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
