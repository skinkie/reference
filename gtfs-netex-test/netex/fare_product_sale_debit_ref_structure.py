from dataclasses import dataclass

from .fare_debit_ref_structure import FareDebitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareProductSaleDebitRefStructure(FareDebitRefStructure):
    pass
