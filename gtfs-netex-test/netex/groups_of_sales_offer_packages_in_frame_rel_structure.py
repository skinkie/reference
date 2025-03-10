from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .group_of_sales_offer_packages import GroupOfSalesOfferPackages

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupsOfSalesOfferPackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "groupsOfSalesOfferPackagesInFrame_RelStructure"

    group_of_sales_offer_packages: list[GroupOfSalesOfferPackages] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
