from dataclasses import dataclass
from .blacklist_ref_structure import BlacklistRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistRef(BlacklistRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
