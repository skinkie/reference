from dataclasses import dataclass

from .customer_account_ref_structure import CustomerAccountRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountRef(CustomerAccountRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
