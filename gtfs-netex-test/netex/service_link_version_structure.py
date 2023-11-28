from dataclasses import dataclass, field
from typing import Optional
from netex.all_modes_enumeration import AllModesEnumeration
from netex.link_version_structure import LinkVersionStructure
from netex.operational_context_ref import OperationalContextRef
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkVersionStructure(LinkVersionStructure):
    """
    Type for SERVICE LINK.

    :ivar from_point_ref: Identifier of SCHEDULED STOP POINT from which
        Link starts.
    :ivar to_point_ref: Identifier of SCHEDULED STOP POINT at which Link
        ends.
    :ivar vehicle_mode:
    :ivar operational_context_ref:
    """
    class Meta:
        name = "ServiceLink_VersionStructure"

    from_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
