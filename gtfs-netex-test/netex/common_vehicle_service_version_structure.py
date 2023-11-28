from dataclasses import dataclass, field
from typing import Optional
from netex.mobility_service_version_structure import MobilityServiceVersionStructure
from netex.online_service_refs_rel_structure import OnlineServiceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommonVehicleServiceVersionStructure(MobilityServiceVersionStructure):
    """
    Type for COMMON VEHICLE SERVICE.

    :ivar booking_required: Whether booking is required.
    :ivar registration_required: Whether registration is required.
    :ivar proposed_by_services: Online servicies proposing this service,
    """
    class Meta:
        name = "CommonVehicleService_VersionStructure"

    booking_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BookingRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    registration_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegistrationRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    proposed_by_services: Optional[OnlineServiceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "proposedByServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
