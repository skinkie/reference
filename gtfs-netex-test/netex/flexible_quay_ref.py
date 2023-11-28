from dataclasses import dataclass
from netex.flexible_quay_ref_structure import FlexibleQuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleQuayRef(FlexibleQuayRefStructure):
    """
    Reference to a FLEXIBLE QUAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
