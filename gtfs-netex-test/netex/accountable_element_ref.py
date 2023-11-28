from dataclasses import dataclass
from netex.accountable_element_ref_structure import AccountableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccountableElementRef(AccountableElementRefStructure):
    """
    Reference to an ACCOUNTABLE ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
