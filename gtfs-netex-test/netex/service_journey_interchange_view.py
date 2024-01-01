from dataclasses import dataclass
from .service_journey_interchange_derived_view_structure import (
    ServiceJourneyInterchangeDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyInterchangeView(
    ServiceJourneyInterchangeDerivedViewStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
