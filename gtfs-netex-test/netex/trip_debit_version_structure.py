from dataclasses import dataclass

from .fare_debit_version_structure import FareDebitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TripDebitVersionStructure(FareDebitVersionStructure):
    class Meta:
        name = "TripDebit_VersionStructure"
