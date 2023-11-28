from dataclasses import dataclass
from netex.coupled_journey_ref_structure import CoupledJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CoupledJourneyRef(CoupledJourneyRefStructure):
    """
    Reference to a COUPLED JOURNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
