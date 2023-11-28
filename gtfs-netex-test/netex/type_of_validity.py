from dataclasses import dataclass, field
from netex.type_of_validity_value_structure import TypeOfValidityValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfValidity(TypeOfValidityValueStructure):
    """A classification of the validity of TYPEs OF FRAME.

    E.g. frames for schedules designed for DAY TYPEs, for specific
    OPERATING DAYs.

    :ivar id: Reference to a TYPE OF VALIDITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
