from dataclasses import dataclass, field
from typing import Optional
from netex.emv_card_ref import EmvCardRef
from netex.mobile_device_ref import MobileDeviceRef
from netex.security_listing_versioned_child_structure import SecurityListingVersionedChildStructure
from netex.smartcard_ref import SmartcardRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumAccessDeviceSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    """
    Type for MEDIUM ACCESS DEVICE SECURITY LISTING.
    """
    class Meta:
        name = "MediumAccessDeviceSecurityListing_VersionedChildStructure"

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
