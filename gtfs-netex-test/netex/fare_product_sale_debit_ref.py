from dataclasses import dataclass

from .fare_product_sale_debit_ref_structure import FareProductSaleDebitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductSaleDebitRef(FareProductSaleDebitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
