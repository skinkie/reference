from dataclasses import dataclass, field
from typing import Optional
from netex.fare_product_ref_structure import FareProductRefStructure
from netex.fare_product_refs_rel_structure import FareProductRefsRelStructure
from netex.preassigned_fare_product_version_structure import PreassignedFareProductVersionStructure
from netex.supplement_product_enumeration import SupplementProductEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SupplementProductVersionStructure(PreassignedFareProductVersionStructure):
    """
    Type for PREASSIGNED FARE PRODUCT.

    :ivar supplement_product_type: Classification of SUPPLEMENT PRODUCT.
        +v1.1
    :ivar supplement_to_fare_product_ref_or_supplement_to:
    """
    class Meta:
        name = "SupplementProduct_VersionStructure"

    supplement_product_type: Optional[SupplementProductEnumeration] = field(
        default=None,
        metadata={
            "name": "SupplementProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_to_fare_product_ref_or_supplement_to: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementToFareProductRef",
                    "type": FareProductRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "supplementTo",
                    "type": FareProductRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
