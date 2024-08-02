from dataclasses import dataclass

from .product_categories_delivery_structure import ProductCategoriesDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductCategoriesDelivery(ProductCategoriesDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
