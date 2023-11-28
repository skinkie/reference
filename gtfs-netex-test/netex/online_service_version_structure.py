from dataclasses import dataclass, field
from typing import Optional
from netex.mobility_service_refs_rel_structure import MobilityServiceRefsRelStructure
from netex.mobility_service_version_structure import MobilityServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceVersionStructure(MobilityServiceVersionStructure):
    """
    Type for ONLINE SERVICE.

    :ivar log_in_required: Whether login  is required to use service.
    :ivar proposing_services:
    """
    class Meta:
        name = "OnlineService_VersionStructure"

    log_in_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LogInRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    proposing_services: Optional[MobilityServiceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "proposingServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
