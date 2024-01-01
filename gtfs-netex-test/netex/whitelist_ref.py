from dataclasses import dataclass
from .whitelist_ref_structure import WhitelistRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WhitelistRef(WhitelistRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
