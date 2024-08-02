from dataclasses import dataclass

from .fare_debit_version_structure import FareDebitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OffenceDebitVersionStructure(FareDebitVersionStructure):
    class Meta:
        name = "OffenceDebit_VersionStructure"
