from dataclasses import dataclass
from netex.fulfilment_method_ref_structure import FulfilmentMethodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodRef(FulfilmentMethodRefStructure):
    """
    Reference to a FULFILMENT METHOD.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
