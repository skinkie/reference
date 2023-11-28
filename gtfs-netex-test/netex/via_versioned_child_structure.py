from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.border_point_ref import BorderPointRef
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_view import DestinationDisplayView
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point_ref import GaragePointRef
from netex.multilingual_string import MultilingualString
from netex.parking_point_ref import ParkingPointRef
from netex.relief_point_ref import ReliefPointRef
from netex.route_point_ref import RoutePointRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.timing_point_ref import TimingPointRef
from netex.via_type_enumeration import ViaTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ViaVersionedChildStructure(VersionedChildStructure):
    """
    A secondary heading  (e.g. ROUTE POINT or other place) showing intermediate
    places on the way to a destination.

    :ivar destination_display_ref_or_destination_display_view_or_name:
    :ivar choice:
    :ivar via_type: Classification of meaning of via:
    """
    class Meta:
        name = "Via_VersionedChildStructure"

    destination_display_ref_or_destination_display_view_or_name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Name",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePointRef",
                    "type": RoutePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    via_type: Optional[ViaTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ViaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
