from dataclasses import dataclass, field
from netex.type_of_mobility_service_value_structure import TypeOfMobilityServiceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMobilityService(TypeOfMobilityServiceValueStructure):
    """A classification of a MOBILITY SERVICE according to its functional purpose.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
