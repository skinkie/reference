from dataclasses import dataclass

from .type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PriceUnitRefStructure(TypeOfValueRefStructure):
    pass
