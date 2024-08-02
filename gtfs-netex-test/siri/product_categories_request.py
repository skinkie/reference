from dataclasses import dataclass

from .product_categories_discovery_request_structure import ProductCategoriesDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductCategoriesRequest(ProductCategoriesDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
