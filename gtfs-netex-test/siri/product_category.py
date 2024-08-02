from dataclasses import dataclass

from .product_category_structure import ProductCategoryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductCategory(ProductCategoryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
