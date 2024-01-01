from dataclasses import dataclass
from .validable_element_price_ref_structure import (
    ValidableElementPriceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementPriceRef(ValidableElementPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
