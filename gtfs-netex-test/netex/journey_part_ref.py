from dataclasses import dataclass
from netex.journey_part_ref_structure import JourneyPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartRef(JourneyPartRefStructure):
    """
    Reference to a JOURNEY PART.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
