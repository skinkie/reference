from dataclasses import dataclass

from .accountable_element_ref_structure import AccountableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DutyPartRefStructure(AccountableElementRefStructure):
    pass
