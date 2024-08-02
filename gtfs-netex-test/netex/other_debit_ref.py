from dataclasses import dataclass

from .other_debit_ref_structure import OtherDebitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDebitRef(OtherDebitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
