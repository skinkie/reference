from dataclasses import dataclass

from .related_journey_structure import RelatedJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RelatedJourney(RelatedJourneyStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
