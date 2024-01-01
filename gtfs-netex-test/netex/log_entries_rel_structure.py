from dataclasses import dataclass
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogEntriesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "logEntries_RelStructure"
