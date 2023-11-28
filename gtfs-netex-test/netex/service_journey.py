from dataclasses import dataclass, field
from netex.service_journey_version_structure import ServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourney(ServiceJourneyVersionStructure):
    """A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE.

    The pattern of working is in principle defined by a SERVICE JOURNEY
    PATTERN. The VIEW includes derived ancillary data from referenced
    entities.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
