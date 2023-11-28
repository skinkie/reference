from dataclasses import dataclass, field
from typing import List
from netex.access import Access
from netex.connection import Connection
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.default_connection import DefaultConnection
from netex.site_connection import SiteConnection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransfersInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CONNECTIONs.
    """
    class Meta:
        name = "transfersInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Connection",
                    "type": Connection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnection",
                    "type": DefaultConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnection",
                    "type": SiteConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
