from dataclasses import dataclass
from netex.operational_context_ref_structure import OperationalContextRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperationalContextRef(OperationalContextRefStructure):
    """
    Reference to an OPERATIONAL CONTEXT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
