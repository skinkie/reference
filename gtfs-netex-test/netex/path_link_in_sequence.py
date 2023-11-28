from dataclasses import dataclass, field
from netex.path_link_in_sequence_versioned_child_structure import PathLinkInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkInSequence(PathLinkInSequenceVersionedChildStructure):
    """
    A step in a Navigation PATH.

    :ivar id: Identifier of ENTITY.
    :ivar order: Order of LINK in sequence.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
