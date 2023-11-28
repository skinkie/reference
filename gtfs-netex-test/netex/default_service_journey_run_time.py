from dataclasses import dataclass, field
from netex.default_service_journey_run_time_versioned_child_structure import DefaultServiceJourneyRunTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultServiceJourneyRunTime(DefaultServiceJourneyRunTimeVersionedChildStructure):
    """The default time taken by a vehicle to traverse a TIMING LINK during a
    SERVICE JOURNEY, for a specified TIME DEMAND TYPE.

    This time may be superseded by the JOURNEY PATTERN RUN TIME or
    VEHICLE JOURNEY RUN TIME if these exist.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
