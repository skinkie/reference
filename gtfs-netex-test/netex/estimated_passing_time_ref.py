from dataclasses import dataclass
from netex.estimated_passing_time_ref_structure import EstimatedPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EstimatedPassingTimeRef(EstimatedPassingTimeRefStructure):
    """
    Reference to an ESTIMATED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
