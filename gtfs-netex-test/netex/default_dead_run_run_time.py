from dataclasses import dataclass, field
from netex.default_dead_run_run_time_versioned_child_structure import DefaultDeadRunRunTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultDeadRunRunTime(DefaultDeadRunRunTimeVersionedChildStructure):
    """The time taken to traverse a TIMING LINK during a DEAD RUN, for a specified
    TIME DEMAND TYPE.

    This time may be superseded by the JOURNEY PATTERN RUN TIME or
    VEHICLE JOURNEY RUN TIME if these exist.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
