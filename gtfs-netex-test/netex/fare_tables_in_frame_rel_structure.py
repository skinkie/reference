from dataclasses import dataclass, field
from typing import Union

from .frame_containment_structure import FrameContainmentStructure
from .priceable_object_version_structure import (
    FareTable,
    FareTableInContext,
)
from .standard_fare_table import StandardFareTable

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareTablesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareTablesInFrame_RelStructure"

    fare_table: list[Union[StandardFareTable, FareTableInContext, FareTable]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
