from dataclasses import dataclass, field
from netex.type_of_product_category_structure import TypeOfProductCategoryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfProductCategory(TypeOfProductCategoryStructure):
    """
    Classification of a PRODUCT CATEGORY.

    :ivar id: Reference to a TYPE OF PRODUCT CATEGORY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
