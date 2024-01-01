from dataclasses import dataclass
from .fare_structure_factor_ref_structure import (
    FareStructureFactorRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeStructureFactorRefStructure(FareStructureFactorRefStructure):
    value: RestrictedVar
