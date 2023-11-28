from dataclasses import dataclass, field
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.customer_purchase_package_element_accesses_rel_structure import CustomerPurchasePackageElementAccessesRelStructure
from netex.customer_purchase_package_prices_rel_structure import CustomerPurchasePackagePricesRelStructure
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from netex.marked_as_enumeration import MarkedAsEnumeration
from netex.sales_offer_package_element_ref import SalesOfferPackageElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageElementVersionStructure(PriceableObjectVersionStructure):
    """
    Type for CUSTOMER PURCHASE PACKAGE ELEMENT.

    :ivar customer_purchase_package_ref:
    :ivar sales_offer_package_element_ref:
    :ivar marked_as: Usage status of the element. +v1.1
    :ivar blocked: Whether the element has been blocked+v1.1
    :ivar element_accesses: VALIDABLE ELEMENTs for  CUSTOMER PURCHASE
        PACKAGE.
    :ivar validity_parameter_assignments: VALIDITY PARAMETER ASSIGNMENTs
        applying to CUSTOMER PURCHASE PACKAGE ELEMENT..
    :ivar prices: PRICEs of CUSTOMER PURCHASE PACKAGE ELEMENT.
    :ivar order: Relative order of element.
    """
    class Meta:
        name = "CustomerPurchasePackageElement_VersionStructure"

    customer_purchase_package_ref: Optional[CustomerPurchasePackageRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_element_ref: Optional[SalesOfferPackageElementRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    marked_as: Optional[MarkedAsEnumeration] = field(
        default=None,
        metadata={
            "name": "MarkedAs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blocked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Blocked",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    element_accesses: Optional[CustomerPurchasePackageElementAccessesRelStructure] = field(
        default=None,
        metadata={
            "name": "elementAccesses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignments: Optional[CustomerPurchaseParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[CustomerPurchasePackagePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
