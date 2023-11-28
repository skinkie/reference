from dataclasses import dataclass, field
from netex.journey_run_time_versioned_child_structure import JourneyRunTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyRunTime(JourneyRunTimeVersionedChildStructure):
    """The time taken to traverse a TIMING LINK in a particular JOURNEY PATTERN,
    for a specified TIME DEMAND TYPE.

    If it exists, it will override the DEFAULT SERVICE JOURNEY RUN TIME
    and DEFAULT DEAD RUN RUN TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
