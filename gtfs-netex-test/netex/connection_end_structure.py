from dataclasses import dataclass, field
from typing import Optional
from netex.all_modes_enumeration import AllModesEnumeration
from netex.authority_ref import AuthorityRef
from netex.operator_ref import OperatorRef
from netex.point_ref_structure import PointRefStructure
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.submode import Submode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConnectionEndStructure:
    """
    Type for a CONNECTION END.

    :ivar transport_mode: MODE of end Point of CONNECTION. Default is
        all modes, MODE of SCHEDULED STOP POINT can be derived.
    :ivar submode: SUBMODE of end Point of CONNECTION. SUBMODE of
        SCHEDULED STOP POINT can be derived.
    :ivar authority_ref_or_operator_ref:
    :ivar scheduled_stop_point_ref_or_vehicle_meeting_point_ref:
    """
    transport_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    submode: Optional[Submode] = field(
        default=None,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref_or_operator_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    scheduled_stop_point_ref_or_vehicle_meeting_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointRef",
                    "type": PointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
