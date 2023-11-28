from dataclasses import dataclass, field
from netex.timing_algorithm_type_value_structure import TimingAlgorithmTypeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingAlgorithmType(TimingAlgorithmTypeValueStructure):
    """
    Classification of a TIMING ALGORITHM.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
