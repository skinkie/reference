from dataclasses import dataclass, field
from netex.journey_layover_structure import JourneyLayoverStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyLayover(JourneyLayoverStructure):
    """Time allowance at the end of each journey on a specified JOURNEY PATTERN, to
    allow for delays and for other purposes.

    This layover supersedes any global layover and may be superseded by
    a specific VEHICLE JOURNEY LAYOVER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
