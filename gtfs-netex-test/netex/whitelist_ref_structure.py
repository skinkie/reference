from dataclasses import dataclass
from .security_list_ref_structure import SecurityListRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WhitelistRefStructure(SecurityListRefStructure):
    value: RestrictedVar
