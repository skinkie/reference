from dataclasses import dataclass, field

from .type_of_driver_permit_value_structure import TypeOfDriverPermitValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDriverPermit(TypeOfDriverPermitValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
