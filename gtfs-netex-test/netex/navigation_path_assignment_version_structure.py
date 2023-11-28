from dataclasses import dataclass, field
from typing import Optional
from netex.connection_ref import ConnectionRef
from netex.default_connection_ref import DefaultConnectionRef
from netex.navigation_path_ref import NavigationPathRef
from netex.parking_ref import ParkingRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.service_site_ref import ServiceSiteRef
from netex.site_connection_ref import SiteConnectionRef
from netex.site_ref import SiteRef
from netex.stop_assignment_version_structure import StopAssignmentVersionStructure
from netex.stop_place_ref import StopPlaceRef
from netex.taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathAssignmentVersionStructure(StopAssignmentVersionStructure):
    """
    Type for a NAVIGATION PATH ASSIGNMENT.
    """
    class Meta:
        name = "NavigationPathAssignment_VersionStructure"

    default_connection_ref_or_site_connection_ref_or_connection_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    navigation_path_ref: Optional[NavigationPathRef] = field(
        default=None,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
