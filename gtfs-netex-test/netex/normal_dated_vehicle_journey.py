from dataclasses import dataclass, field
from netex.normal_dated_vehicle_journey_version_structure import NormalDatedVehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NormalDatedVehicleJourney(NormalDatedVehicleJourneyVersionStructure):
    """
    A DATED VEHICLE JOURNEY identical to a long-term planned VEHICLE JOURNEY,
    possibly updated according to short-term modifications of the PRODUCTION PLAN
    decided by the control staff.

    :ivar id: Identifier of NORMAL DATED VEHICLE JORUNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
