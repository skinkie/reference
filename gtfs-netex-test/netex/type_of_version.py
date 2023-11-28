from dataclasses import dataclass, field
from netex.type_of_version_value_structure import TypeOfVersionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfVersion(TypeOfVersionValueStructure):
    """
    A classification of the VERSIONs.

    :ivar id: Reference to a TYPE OF VERSION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
