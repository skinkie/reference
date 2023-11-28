from dataclasses import dataclass, field
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.customer_account_ref import CustomerAccountRef
from netex.customer_purchase_package_elements_rel_structure import CustomerPurchasePackageElementsRelStructure
from netex.customer_purchase_package_prices_rel_structure import CustomerPurchasePackagePricesRelStructure
from netex.customer_purchase_package_status_enumeration import CustomerPurchasePackageStatusEnumeration
from netex.customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from netex.customer_ref import CustomerRef
from netex.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.emv_card_ref import EmvCardRef
from netex.fare_contract_ref import FareContractRef
from netex.medium_application_instance_ref import MediumApplicationInstanceRef
from netex.mobile_device_ref import MobileDeviceRef
from netex.private_code import PrivateCode
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.sales_transaction_ref import SalesTransactionRef
from netex.sales_transaction_refs_rel_structure import SalesTransactionRefsRelStructure
from netex.smartcard_ref import SmartcardRef
from netex.travel_documents_rel_structure import TravelDocumentsRelStructure
from netex.travel_specification_summary_view import TravelSpecificationSummaryView
from netex.travel_specifications_rel_structure import TravelSpecificationsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageVersionStructure(PriceableObjectVersionStructure):
    """
    Type for CUSTOMER PURCHASE PACKAGE.

    :ivar private_code:
    :ivar sales_offer_package_ref:
    :ivar customer_ref:
    :ivar customer_account_ref:
    :ivar fare_contract_ref:
    :ivar customer_purchase_package_status: Status of CUSTOMER PURCHASE
        PACKAGE +v1.1
    :ivar travel_specification_summary_view:
    :ivar travel_specifications: TRAVEL SPEECIFICATIONs for FARE
        CONTRACT.
    :ivar validity_parameter_assignments: PARAMETER ASSIGNMENTs applying
        to whole CUSTOMER PURCHASE PACKAGE.
    :ivar distribution_assignments: DiISTRIBUTION ASSIGNMENTS for
        CUSTOMER PURCHASE PACKAGE.
    :ivar customer_purchase_package_elements: CUSTOMER PURCHASE PACKAGE
        ELEMENTs in CUSTOMER PURCHASE PACKAGE.
    :ivar sales_transaction_ref:
    :ivar sales_transactions: SALES TRANSACTIONs for CUSTOMER PURCHASE
        PACKAGE.
    :ivar prices: PRICEs of CUSTOMER PURCHASE PACKAGE ELEMENT.
    :ivar travel_documents: TRAVEL DOCUMENTs associated with package
    :ivar mobile_device_ref_or_emv_card_ref_or_smartcard_ref:
    :ivar medium_application_instance_ref:
    """
    class Meta:
        name = "CustomerPurchasePackage_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_status: Optional[CustomerPurchasePackageStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification_summary_view: Optional[TravelSpecificationSummaryView] = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specifications: Optional[TravelSpecificationsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
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
    distribution_assignments: Optional[DistributionAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_elements: Optional[CustomerPurchasePackageElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_ref: Optional[SalesTransactionRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transactions: Optional[SalesTransactionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "salesTransactions",
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
    travel_documents: Optional[TravelDocumentsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobile_device_ref_or_emv_card_ref_or_smartcard_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobileDeviceRef",
                    "type": MobileDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EmvCardRef",
                    "type": EmvCardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SmartcardRef",
                    "type": SmartcardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    medium_application_instance_ref: Optional[MediumApplicationInstanceRef] = field(
        default=None,
        metadata={
            "name": "MediumApplicationInstanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
