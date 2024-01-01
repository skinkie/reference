from dataclasses import dataclass
from .dated_service_journey_version_structure import (
    DatedServiceJourneyVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedServiceJourney(DatedServiceJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
