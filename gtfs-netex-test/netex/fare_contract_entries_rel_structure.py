from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, ForwardRef, List, Optional, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account_ref import CustomerAccountRef
from .customer_purchase_package_elements_rel_structure import CustomerPurchasePackageElementsRelStructure
from .customer_purchase_package_prices_rel_structure import CustomerPurchasePackagePricesRelStructure
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .customer_purchase_package_status_enumeration import CustomerPurchasePackageStatusEnumeration
from .customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from .customer_ref import CustomerRef
from .distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from .emv_card_ref import EmvCardRef
from .fare_contract_entry import FareContractEntry
from .fare_contract_entry_ref import FareContractEntryRef
from .fare_contract_entry_version_structure import FareContractEntryVersionStructure
from .fare_contract_ref import FareContractRef
from .medium_application_instance_ref import MediumApplicationInstanceRef
from .mobile_device_ref import MobileDeviceRef
from .multilingual_string import MultilingualString
from .offered_travel_specification import OfferedTravelSpecification
from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .organisational_unit_ref import OrganisationalUnitRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .point_version_structure import PointVersionStructure
from .price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from .price_unit_ref import PriceUnitRef
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .private_code import PrivateCode
from .private_code_structure import PrivateCodeStructure
from .requested_travel_specification import RequestedTravelSpecification
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .retail_device_ref import RetailDeviceRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .sales_transaction_ref import SalesTransactionRef
from .sales_transaction_refs_rel_structure import SalesTransactionRefsRelStructure
from .smartcard_ref import SmartcardRef
from .travel_documents_rel_structure import TravelDocumentsRelStructure
from .travel_specification_1 import TravelSpecification1
from .travel_specification_2 import TravelSpecification2
from .travel_specification_ref import TravelSpecificationRef
from .travel_specification_summary_view import TravelSpecificationSummaryView
from .travel_specifications_rel_structure import TravelSpecificationsRelStructure
from .type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractEntriesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareContractEntries_RelStructure"

    fare_contract_entry_ref_or_travel_specification_ref_or_fare_contract_entry_or_travel_specification: List[
        Union[SalesTransactionRef, OfferedTravelSpecificationRef, RequestedTravelSpecificationRef, TravelSpecificationRef, FareContractEntryRef, "SalesTransaction", OfferedTravelSpecification, RequestedTravelSpecification, TravelSpecification1, TravelSpecification2, FareContractEntry]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesTransactionRef",
                    "type": SalesTransactionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecificationRef",
                    "type": RequestedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationRef",
                    "type": TravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntryRef",
                    "type": FareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransaction",
                    "type": ForwardRef("SalesTransaction"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecification",
                    "type": RequestedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification",
                    "type": TravelSpecification1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification_",
                    "type": TravelSpecification2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntry_",
                    "type": FareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CustomerPurchasePackageVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "CustomerPurchasePackage_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_package_status: Optional[CustomerPurchasePackageStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specification_summary_view: Optional[TravelSpecificationSummaryView] = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specifications: Optional[TravelSpecificationsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments: Optional[CustomerPurchaseParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignments: Optional[DistributionAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_package_elements: Optional[CustomerPurchasePackageElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_transaction_ref: Optional[SalesTransactionRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_transactions: Optional[SalesTransactionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "salesTransactions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[CustomerPurchasePackagePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_documents: Optional[TravelDocumentsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medium_access_device_ref: Optional[Union[MobileDeviceRef, EmvCardRef, SmartcardRef]] = field(
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
        },
    )
    medium_application_instance_ref: Optional[MediumApplicationInstanceRef] = field(
        default=None,
        metadata={
            "name": "MediumApplicationInstanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_package_entries: Optional[FareContractEntriesRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackageEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class CustomerPurchasePackage(CustomerPurchasePackageVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerPurchasePackages_RelStructure"

    customer_purchase_package_or_customer_purchase_package_ref: List[Union[CustomerPurchasePackage, CustomerPurchasePackageRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackage",
                    "type": CustomerPurchasePackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SalesTransactionVersionStructure(FareContractEntryVersionStructure):
    class Meta:
        name = "SalesTransaction_VersionStructure"

    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rule_step_results: Optional[PriceRuleStepResultsRelStructure] = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    card_number: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "CardNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specifications: Optional[TravelSpecificationsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: Optional[CustomerPurchasePackagesRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_documents: Optional[TravelDocumentsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_point_ref: Optional[PointVersionStructure] = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CollectionNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisational_unit_ref: Optional[OrganisationalUnitRef] = field(
        default=None,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_device_ref: Optional[RetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class SalesTransaction(SalesTransactionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
