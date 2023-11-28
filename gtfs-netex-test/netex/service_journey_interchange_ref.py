from dataclasses import dataclass
from netex.service_journey_interchange_ref_structure import ServiceJourneyInterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchangeRef(ServiceJourneyInterchangeRefStructure):
    """
    Reference to a SERVICE JOURNEY INTERCHANGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
