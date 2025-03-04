from dataclasses import dataclass

from .customer_account_version_structure import CustomerAccountVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerAccount(CustomerAccountVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
