from dataclasses import dataclass
from netex.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurposeOfJourneyPartitionRefStructure(TypeOfValueRefStructure):
    """
    Type for a PURPOSE OF JOURNEY PARTITION.
    """
