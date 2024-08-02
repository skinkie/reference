from dataclasses import dataclass

from .fare_debit_version_structure import FareDebitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDebitVersionStructure(FareDebitVersionStructure):
    class Meta:
        name = "OtherDebit_VersionStructure"
