from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfJourneyPartitionValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "PurposeOfJourneyPartition_ValueStructure"
