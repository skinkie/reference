from dataclasses import dataclass, field
from netex.class_of_use_value_structure import ClassOfUseValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassOfUse(ClassOfUseValueStructure):
    """
    Defines an Classification of users who may make use of a component or amenity.

    :ivar id: Identifier of  CLASS OF USE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
