from dataclasses import dataclass

from .type_of_product_category_structure import TypeOfProductCategoryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfProductCategory(TypeOfProductCategoryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
