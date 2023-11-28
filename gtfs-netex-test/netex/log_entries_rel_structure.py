from dataclasses import dataclass
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LogEntriesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of  LOG ENTries   +v1.1.
    """
    class Meta:
        name = "logEntries_RelStructure"
