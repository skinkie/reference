from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PaymentByMobileStructure:
    """
    Type for Payment By Mobile details.

    :ivar phone_number_to_pay: Phone number to call or text to pay.
    :ivar support_phone_number: Phone number for support.
    :ivar payment_url: URL to make paymnet.
    :ivar payment_app_download_url: URL to downlaod app to pay.
    """
    phone_number_to_pay: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumberToPay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    support_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupportPhoneNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_app_download_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentAppDownloadUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
