from dataclasses import dataclass

from .purpose_of_journey_partition_value_structure import PurposeOfJourneyPartitionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PurposeOfJourneyPartition(PurposeOfJourneyPartitionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
