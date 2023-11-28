from dataclasses import dataclass, field
from netex.codespace_structure import CodespaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Codespace(CodespaceStructure):
    """A system for uniquely identifying objects of a given type.

    Used for the distributed management of objects from many different
    sources. For example eachregion of a country may be given a
    different codespace to use when allocating stop identifieres which
    will be unique within a country.

    :ivar id: Identifier of CODESPACE. Maybe the same as Xmlns prefix.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
