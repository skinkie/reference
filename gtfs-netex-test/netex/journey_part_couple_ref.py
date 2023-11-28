from dataclasses import dataclass
from netex.journey_part_couple_ref_structure import JourneyPartCoupleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartCoupleRef(JourneyPartCoupleRefStructure):
    """
    Reference to a JOURNEY PART COUPLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
