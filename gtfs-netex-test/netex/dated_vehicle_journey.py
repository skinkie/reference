from dataclasses import dataclass, field
from netex.dated_vehicle_journey_version_structure import DatedVehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedVehicleJourney(DatedVehicleJourneyVersionStructure):
    """
    A particular journey of a vehicle on a particular OPERATING DAY including all
    modifications possibly decided by the control staff.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
