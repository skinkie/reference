from dataclasses import dataclass
from netex.service_journey_interchange_derived_view_structure import ServiceJourneyInterchangeDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchangeView(ServiceJourneyInterchangeDerivedViewStructure):
    """
    Simplified  view of SERVICE JOURNEY INTERCHANGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
