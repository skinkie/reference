from dataclasses import dataclass, field
from netex.whitelist_version_structure import WhitelistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Whitelist(WhitelistVersionStructure):
    """
    A list of  items (TRAVEL DOCUMENTs, CONTRACTs, etc) explicitly approved for
    processing.+v1.1.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
