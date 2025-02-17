from dataclasses import dataclass

from .coupled_journey_version_structure import CoupledJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CoupledJourney(CoupledJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
