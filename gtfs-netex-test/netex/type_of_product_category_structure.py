from dataclasses import dataclass, field
from typing import Optional
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfProductCategoryStructure(TypeOfEntityVersionStructure):
    """
    Type for a TYPE OF PRODUCT CATEGORY.

    :ivar external_product_category_ref: An alternative code that
        uniquely identifies the PRODUCT CATEGORY. Specifically for use
        in AVMS systems that require an alias, if code is different from
        main identifier. For VDV compatibility.
    """
    external_product_category_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
