from dataclasses import dataclass
from netex.subscribing_ref_structure import SubscribingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SubscribingRef(SubscribingRefStructure):
    """Reference to a SUBSCRIBING usage parameter.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
