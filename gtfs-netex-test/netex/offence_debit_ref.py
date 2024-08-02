from dataclasses import dataclass

from .offence_debit_ref_structure import OffenceDebitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OffenceDebitRef(OffenceDebitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
