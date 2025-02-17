from dataclasses import dataclass

from .journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleJourneyRefStructure(JourneyRefStructure):
    pass
