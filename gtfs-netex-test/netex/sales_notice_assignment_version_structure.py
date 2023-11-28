from dataclasses import dataclass, field
from typing import Optional
from netex.country_ref import CountryRef
from netex.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.notice_assignment_version_structure import NoticeAssignmentVersionStructure
from netex.sales_offer_package_ref import SalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesNoticeAssignmentVersionStructure(NoticeAssignmentVersionStructure):
    """
    Type for SALES NOTICE ASSIGNMENT.
    """
    class Meta:
        name = "SalesNoticeAssignment_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
