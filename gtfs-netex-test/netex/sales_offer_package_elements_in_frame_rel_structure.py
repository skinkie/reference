from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .sales_offer_package_element import SalesOfferPackageElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesOfferPackageElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "salesOfferPackageElementsInFrame_RelStructure"

    sales_offer_package_element: list[SalesOfferPackageElement] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
