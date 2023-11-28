from dataclasses import dataclass
from netex.observed_passing_time_ref_structure import ObservedPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ObservedPassingTimeRef(ObservedPassingTimeRefStructure):
    """
    Reference to an OBSERVED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
