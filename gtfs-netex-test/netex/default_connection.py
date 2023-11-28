from dataclasses import dataclass, field
from netex.default_connection_version_structure import DefaultConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultConnection(DefaultConnectionVersionStructure):
    """
    Specifies the default transfer times to transfer between MODEs and / or
    OPERATORs within a region.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
