from dataclasses import dataclass, field
from netex.authority_version_structure import AuthorityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Authority(AuthorityVersionStructure):
    """
    The ORGANISATION under which the responsibility of organising the transport
    service in a certain area is placed.

    :ivar id: Identifier of AUTHORITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
