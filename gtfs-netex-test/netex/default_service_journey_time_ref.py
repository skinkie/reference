from dataclasses import dataclass
from .default_service_journey_time_ref_structure import (
    DefaultServiceJourneyTimeRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultServiceJourneyTimeRef(DefaultServiceJourneyTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
