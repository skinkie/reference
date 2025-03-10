from dataclasses import dataclass

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LogEntriesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "logEntries_RelStructure"
