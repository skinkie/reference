from dataclasses import dataclass, field
from netex.dated_service_journey_version_structure import DatedServiceJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedServiceJourney(DatedServiceJourneyVersionStructure):
    """A particular journey of a vehicle on a particular OPERATING DAY including
    all modifications possibly decided by the control staff.

    The VIEW includes derived ancillary data from referenced entities.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
