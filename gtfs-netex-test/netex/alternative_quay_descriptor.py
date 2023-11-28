from dataclasses import dataclass, field
from netex.alternative_quay_descriptor_versioned_child_structure import AlternativeQuayDescriptorVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeQuayDescriptor(AlternativeQuayDescriptorVersionedChildStructure):
    """
    An element of a STOP PLACE describing part of its structure.

    :ivar type_of_name: Type of Name.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    type_of_name: str = field(
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "required": True,
        }
    )
