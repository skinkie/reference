from dataclasses import dataclass
from .luggage_allowance_ref_structure import LuggageAllowanceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageAllowanceRef(LuggageAllowanceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
