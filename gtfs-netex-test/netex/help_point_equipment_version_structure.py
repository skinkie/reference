from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.accessibility_assessment import AccessibilityAssessment
from netex.passenger_equipment_version_structure import PassengerEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HelpPointEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    """
    Type for a HELP POINT EQUIPMENT.

    :ivar accessibility_assessment:
    :ivar height_from_ground: Height of HELP POINT from ground.
    :ivar phone: Whether help point is a phone.
    :ivar induction_loop: Whether there is an induction loop.
    :ivar induction_loop_sign: Whether there is an indication that there
        is an induction loop.
    :ivar stop_request_button: Whether there is a button to request a
        vehicle to stop.
    :ivar stop_request_timeout: Timeout for a stop request. After this
        interval after pressing request button  a request will be
        ignored and a new request must be made.
    """
    class Meta:
        name = "HelpPointEquipment_VersionStructure"

    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_from_ground: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromGround",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    phone: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    induction_loop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    induction_loop_sign: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InductionLoopSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_request_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopRequestButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_request_timeout: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StopRequestTimeout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
