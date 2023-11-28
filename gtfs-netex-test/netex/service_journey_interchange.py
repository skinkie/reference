from dataclasses import dataclass, field
from netex.service_journey_interchange_version_structure import ServiceJourneyInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchange(ServiceJourneyInterchangeVersionStructure):
    """
    The scheduled possibility for transfer of passengers between two SERVICE
    JOURNEYs at the same or different STOP POINTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
