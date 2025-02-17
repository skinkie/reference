from dataclasses import dataclass

from .fare_debit_version_structure import FareDebitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareProductSaleDebitVersionStructure(FareDebitVersionStructure):
    class Meta:
        name = "FareProductSaleDebit_VersionStructure"
