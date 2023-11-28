from dataclasses import dataclass
from netex.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfSalesOfferPackageRefStructure(TypeOfValueRefStructure):
    """
    Type for Reference to a TYPE OF SALES OFFER PACKAGE.
    """
