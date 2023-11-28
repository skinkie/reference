from dataclasses import dataclass, field
from netex.type_of_zone_value_structure import TypeOfZoneValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfZone(TypeOfZoneValueStructure):
    """
    Classification of a ZONe.

    :ivar id: Reference to a TYPE OF ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
