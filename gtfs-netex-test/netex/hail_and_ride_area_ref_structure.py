from dataclasses import dataclass
from netex.flexible_quay_ref_structure import FlexibleQuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HailAndRideAreaRefStructure(FlexibleQuayRefStructure):
    """
    Type for Unique Reference to a HAIL AND RIDE AREA.
    """
