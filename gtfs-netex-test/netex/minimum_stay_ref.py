from dataclasses import dataclass
from netex.minimum_stay_ref_structure import MinimumStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MinimumStayRef(MinimumStayRefStructure):
    """
    Reference to a MINIMUM STAY PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
