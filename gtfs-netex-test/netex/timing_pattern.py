from dataclasses import dataclass, field
from netex.timing_pattern_version_structure import TimingPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPattern(TimingPatternVersionStructure):
    """
    The subset of a JOURNEY PATTERN made up only of TIMING POINTs IN JOURNEY
    PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
