from dataclasses import dataclass

from .type_of_customer_account_version_structure import TypeOfCustomerAccountVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfCustomerAccount(TypeOfCustomerAccountVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
