from dataclasses import dataclass

from .whitelist_ref_structure import WhitelistRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class WhitelistRef(WhitelistRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
