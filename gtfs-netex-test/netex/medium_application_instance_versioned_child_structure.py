from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.customer_account_ref import CustomerAccountRef
from netex.emv_card_ref import EmvCardRef
from netex.mobile_device_ref import MobileDeviceRef
from netex.multilingual_string import MultilingualString
from netex.service_access_code_ref import ServiceAccessCodeRef
from netex.smartcard_ref import SmartcardRef
from netex.travel_document_ref import TravelDocumentRef
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumApplicationInstanceVersionedChildStructure(VersionedChildStructure):
    """
    Type for MEDIUM APPLICATION INSTANCE restricts id.

    :ivar name: Name for application instance.
    :ivar identity_token: Secure token used to identify MEDIUM
        APPLICATION INSTANCE DEVICE.
    :ivar mobile_device_ref_or_emv_card_ref_or_smartcard_ref:
    :ivar customer_account_ref:
    :ivar type_of_travel_document_ref:
    :ivar service_access_code_ref_or_travel_document_ref:
    """
    class Meta:
        name = "MediumApplicationInstance_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    identity_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityToken",
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
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_access_code_ref_or_travel_document_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceAccessCodeRef",
                    "type": ServiceAccessCodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
