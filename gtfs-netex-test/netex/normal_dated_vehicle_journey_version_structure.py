from dataclasses import dataclass, field
from typing import Optional
from .dated_vehicle_journey_version_structure import (
    DatedVehicleJourneyVersionStructure,
)
from .service_alteration_enumeration import ServiceAlterationEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NormalDatedVehicleJourneyVersionStructure(
    DatedVehicleJourneyVersionStructure
):
    class Meta:
        name = "NormalDatedVehicleJourney_VersionStructure"

    service_alteration_type: Optional[ServiceAlterationEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceAlterationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
