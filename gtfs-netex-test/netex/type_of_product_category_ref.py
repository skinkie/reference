from dataclasses import dataclass

from .type_of_product_category_ref_structure import TypeOfProductCategoryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfProductCategoryRef(TypeOfProductCategoryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
