from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .sales_offer_package_substitution import SalesOfferPackageSubstitution

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesOfferPackageSubstitutionsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "salesOfferPackageSubstitutionsInFrame_RelStructure"

    sales_offer_package_substitution: list[SalesOfferPackageSubstitution] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageSubstitution",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
