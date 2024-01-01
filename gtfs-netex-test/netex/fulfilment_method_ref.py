from dataclasses import dataclass
from .fulfilment_method_ref_structure import FulfilmentMethodRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethodRef(FulfilmentMethodRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
