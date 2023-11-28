from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.destination_display_ref import DestinationDisplayRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.multilingual_string import MultilingualString
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.topographic_place_view import TopographicPlaceView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfServicesEndPointDerivedViewStructure(DerivedViewStructure):
    """
    Type for SIMPLE SCHEDULED STOP POINT VIEW.

    :ivar name: Name of Stop Point.
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar destination_display_ref:
    :ivar topographic_place_view:
    """
    class Meta:
        name = "GroupOfServicesEndPoint_DerivedViewStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
