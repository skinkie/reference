from dataclasses import dataclass
from .preassigned_fare_product_ref_structure import (
    PreassignedFareProductRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplementProductRefStructure(PreassignedFareProductRefStructure):
    value: RestrictedVar
