from dataclasses import dataclass
from .type_of_fare_structure_factor_ref_structure import (
    TypeOfFareStructureFactorRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureFactorRef(TypeOfFareStructureFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
