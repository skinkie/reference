from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassRefStructure:
    """
    Type for a reference to the Class of a ENTITY.

    :ivar value:
    :ivar name_of_class: Name of referenced Class.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    name_of_class: str = field(
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
            "required": True,
        }
    )
