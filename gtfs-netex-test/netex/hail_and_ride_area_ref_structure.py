from dataclasses import dataclass

from .flexible_quay_ref_structure import FlexibleQuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HailAndRideAreaRefStructure(FlexibleQuayRefStructure):
    pass
