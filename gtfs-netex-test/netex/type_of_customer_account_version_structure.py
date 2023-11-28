from dataclasses import dataclass
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfCustomerAccountVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF CUSTOMER ACCOUNT.
    """
    class Meta:
        name = "TypeOfCustomerAccount_VersionStructure"
