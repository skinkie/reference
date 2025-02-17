from dataclasses import dataclass, field
from typing import Union

from .access import Access
from .connection import Connection
from .containment_aggregation_structure import ContainmentAggregationStructure
from .default_connection import DefaultConnection
from .site_connection import SiteConnection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransfersInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transfersInFrame_RelStructure"

    transfer: list[Union[Connection, DefaultConnection, SiteConnection, Access]] = field(
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
        },
    )
