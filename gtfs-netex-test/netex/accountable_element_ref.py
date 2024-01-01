from dataclasses import dataclass
from .accountable_element_ref_structure import AccountableElementRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccountableElementRef(AccountableElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
