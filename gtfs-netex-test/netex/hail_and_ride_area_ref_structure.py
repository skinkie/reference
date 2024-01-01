from dataclasses import dataclass
from .flexible_quay_ref_structure import FlexibleQuayRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HailAndRideAreaRefStructure(FlexibleQuayRefStructure):
    value: RestrictedVar
