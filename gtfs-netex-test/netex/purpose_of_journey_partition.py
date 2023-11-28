from dataclasses import dataclass, field
from netex.purpose_of_journey_partition_value_structure import PurposeOfJourneyPartitionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurposeOfJourneyPartition(PurposeOfJourneyPartitionValueStructure):
    """
    An operational purpose changing within a JOURNEY PATTERN and with this
    subdividing the SERVICE JOURNEY into JOURNEY PARTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
