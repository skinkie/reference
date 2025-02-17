from dataclasses import dataclass

from .fare_debit_version_structure import FareDebitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BookingDebitVersionStructure(FareDebitVersionStructure):
    class Meta:
        name = "BookingDebit_VersionStructure"
