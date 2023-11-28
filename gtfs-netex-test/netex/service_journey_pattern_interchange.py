from dataclasses import dataclass, field
from netex.service_journey_pattern_interchange_version_structure import ServiceJourneyPatternInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyPatternInterchange(ServiceJourneyPatternInterchangeVersionStructure):
    """A recognised/organised possibility for passengers to change public transport
    vehicles using two STOP POINTs (which may be identical) on two particular
    SERVICE JOURNEY PATTERNs, including the maximum wait duration allowed and the
    standard to be aimed at.

    These may supersede the times given for the DEFAULT INTERCHANGE.
    Schedulers may use this entity for synchronisation of journeys.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
