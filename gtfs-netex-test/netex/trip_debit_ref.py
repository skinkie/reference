from dataclasses import dataclass

from .trip_debit_ref_structure import TripDebitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TripDebitRef(TripDebitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
