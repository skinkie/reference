from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.sales_offer_package import SalesOfferPackage

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackagesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of SALES OFFER PACKAGE.
    """
    class Meta:
        name = "salesOfferPackagesInFrame_RelStructure"

    sales_offer_package: List[SalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
