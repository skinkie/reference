from dataclasses import dataclass, field
from typing import Optional
from netex.dated_vehicle_journey_version_structure import DatedVehicleJourneyVersionStructure
from netex.service_alteration_enumeration import ServiceAlterationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NormalDatedVehicleJourneyVersionStructure(DatedVehicleJourneyVersionStructure):
    """
    Type for NORMAL DATED VEHICLE JOURNEY.

    :ivar service_alteration_type: Type of Service alteration. Default
        is planned.
    """
    class Meta:
        name = "NormalDatedVehicleJourney_VersionStructure"

    service_alteration_type: Optional[ServiceAlterationEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceAlterationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
