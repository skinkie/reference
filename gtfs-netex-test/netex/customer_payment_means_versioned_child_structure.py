from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.customer_account_ref import CustomerAccountRef
from netex.emv_card_ref import EmvCardRef
from netex.mobile_device_ref import MobileDeviceRef
from netex.multilingual_string import MultilingualString
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.smartcard_ref import SmartcardRef
from netex.type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPaymentMeansVersionedChildStructure(VersionedChildStructure):
    """
    Type for CUSTOMER PAYMENT MEANS restricts id.

    :ivar name: Name of PAYMENT MEANS.
    :ivar customer_account_ref:
    :ivar mobile_device_ref_or_emv_card_ref_or_smartcard_ref:
    :ivar payment_method: Method of payment used,
    :ivar type_of_payment_method_ref:
    :ivar last_verified_date: Dat that means was last verified by an
        authentication process.
    """
    class Meta:
        name = "CustomerPaymentMeans_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    last_verified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastVerifiedDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
