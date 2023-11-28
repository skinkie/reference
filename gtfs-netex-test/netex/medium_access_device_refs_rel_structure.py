from dataclasses import dataclass, field
from typing import Optional
from netex.emv_card_ref import EmvCardRef
from netex.mobile_device_ref import MobileDeviceRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.smartcard_ref import SmartcardRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumAccessDeviceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of MEDIUM ACCESS DEVICEs.
    """
    class Meta:
        name = "mediumAccessDeviceRefs_RelStructure"

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
