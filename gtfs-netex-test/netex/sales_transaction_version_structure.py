from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.customer_purchase_packages_rel_structure import CustomerPurchasePackagesRelStructure
from netex.fare_contract_entry_version_structure import FareContractEntryVersionStructure
from netex.multilingual_string import MultilingualString
from netex.organisational_unit_ref import OrganisationalUnitRef
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.point_version_structure import PointVersionStructure
from netex.price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from netex.price_unit_ref import PriceUnitRef
from netex.private_code_structure import PrivateCodeStructure
from netex.retail_device_ref import RetailDeviceRef
from netex.travel_documents_rel_structure import TravelDocumentsRelStructure
from netex.travel_specifications_rel_structure import TravelSpecificationsRelStructure
from netex.type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesTransactionVersionStructure(FareContractEntryVersionStructure):
    """
    Type for SALES TRANSACTION.

    :ivar amount: PRICE amount. in specified currency.
    :ivar currency: Currency of Price ISO 4217.
    :ivar price_unit_ref:
    :ivar units: Other units for PRICE (If not in a currency).
    :ivar rule_step_results: Interim amounts for any pricing rules
        applied to derive price , for example VAT amount  charged.
        +v1.1
    :ivar payment_method: Method of payment used,
    :ivar type_of_payment_method_ref:
    :ivar card_number: Card number used,
    :ivar travel_specifications: Travel Specifcations bought  by Salles
        Transaction
    :ivar customer_purchase_packages: Customer Pucrhase PAckages ought
        by Salles Transaction
    :ivar travel_documents: TRAVEL DOCUMENTS materialising SALES
        TRANSACTION.
    :ivar collection_point_ref: Point at which to be collected.
    :ivar collection_note: Note on how to collect.
    :ivar organisational_unit_ref:
    :ivar retail_device_ref:
    """
    class Meta:
        name = "SalesTransaction_VersionStructure"

    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
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
        }
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rule_step_results: Optional[PriceRuleStepResultsRelStructure] = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    card_number: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "CardNumber",
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
    customer_purchase_packages: Optional[CustomerPurchasePackagesRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
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
    collection_point_ref: Optional[PointVersionStructure] = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    collection_note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CollectionNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisational_unit_ref: Optional[OrganisationalUnitRef] = field(
        default=None,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_device_ref: Optional[RetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
