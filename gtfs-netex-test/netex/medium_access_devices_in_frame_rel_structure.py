from dataclasses import dataclass, field
from typing import List
from netex.emv_card import EmvCard
from netex.frame_containment_structure import FrameContainmentStructure
from netex.mobile_device import MobileDevice
from netex.smartcard import Smartcard

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumAccessDevicesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CUSTOMER PURCHASE PACKAGE.
    """
    class Meta:
        name = "mediumAccessDevicesInFrame_RelStructure"

    emv_card_or_smartcard_or_mobile_device: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EmvCard",
                    "type": EmvCard,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Smartcard",
                    "type": Smartcard,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobileDevice",
                    "type": MobileDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
