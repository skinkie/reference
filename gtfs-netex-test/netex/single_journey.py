from dataclasses import dataclass
from .single_journey_version_structure import SingleJourneyVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourney(SingleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
