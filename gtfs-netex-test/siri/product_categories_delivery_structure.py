from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_discovery_delivery_structure import AbstractDiscoveryDeliveryStructure
from .extensions_1 import Extensions1
from .product_category import ProductCategory

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductCategoriesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    product_category: List[ProductCategory] = field(
        default_factory=list,
        metadata={
            "name": "ProductCategory",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
