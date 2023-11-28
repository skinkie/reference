from dataclasses import dataclass, field
from typing import Optional
from netex.fare_product_version_structure import FareProductVersionStructure
from netex.general_group_of_entities import GeneralGroupOfEntities
from netex.general_group_of_entities_ref import GeneralGroupOfEntitiesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ThirdPartyProductVersionStructure(FareProductVersionStructure):
    """
    Type for THIRD PARTY PRODUCT.
    """
    class Meta:
        name = "ThirdPartyProduct_VersionStructure"

    general_group_of_entities_ref_or_general_group_of_entities: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeneralGroupOfEntitiesRef",
                    "type": GeneralGroupOfEntitiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
