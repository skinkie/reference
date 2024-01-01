from dataclasses import dataclass
from .security_list_version_structure import SecurityListVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WhitelistVersionStructure(SecurityListVersionStructure):
    class Meta:
        name = "Whitelist_VersionStructure"
