from dataclasses import dataclass, field
from typing import List
from netex.access_right_in_product import AccessRightInProduct
from netex.access_right_in_product_ref import AccessRightInProductRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightsInProductRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of ACCESS RIGHT IN PRODUCTs.
    """
    class Meta:
        name = "accessRightsInProduct_RelStructure"

    access_right_in_product_ref_or_access_right_in_product: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProduct",
                    "type": AccessRightInProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
