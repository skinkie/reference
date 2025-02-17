from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RelationshipRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name_of_class: str = field(
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
            "required": True,
        }
    )
