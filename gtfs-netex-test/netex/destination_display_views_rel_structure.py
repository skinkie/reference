from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_view import DestinationDisplayView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayViewsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DSETINATION DISPLAY VIEWs.
    """
    class Meta:
        name = "destinationDisplayViews_RelStructure"

    destination_display_ref_or_destination_display_view: List[object] = field(
        default_factory=list,
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
            ),
        }
    )
