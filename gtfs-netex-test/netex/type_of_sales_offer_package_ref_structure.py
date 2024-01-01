from dataclasses import dataclass
from .type_of_value_ref_structure import TypeOfValueRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfSalesOfferPackageRefStructure(TypeOfValueRefStructure):
    value: RestrictedVar
