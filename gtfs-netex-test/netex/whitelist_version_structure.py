from dataclasses import dataclass
from netex.security_list_version_structure import SecurityListVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WhitelistVersionStructure(SecurityListVersionStructure):
    """Type for WHITELIST.

    +v1.1
    """
    class Meta:
        name = "Whitelist_VersionStructure"
