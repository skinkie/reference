from dataclasses import dataclass, field
from typing import Optional, Union

from .connection_ref import ConnectionRef
from .default_connection_ref import DefaultConnectionRef
from .navigation_path_ref import NavigationPathRef
from .parking_ref import ParkingRef
from .point_of_interest_ref import PointOfInterestRef
from .service_site_ref import ServiceSiteRef
from .site_connection_ref import SiteConnectionRef
from .site_navigation_path_ref import SiteNavigationPathRef
from .site_ref import SiteRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPathAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "NavigationPathAssignment_VersionStructure"

    connection_ref: Optional[Union[DefaultConnectionRef, SiteConnectionRef, ConnectionRef]] = field(
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
        },
    )
    site_ref_or_stop_place_ref: Optional[Union[ParkingRef, PointOfInterestRef, TaxiRankRef, StopPlaceRef, ServiceSiteRef, SiteRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
        },
    )
    site_navigation_path_ref_or_navigation_path_ref: Optional[Union[SiteNavigationPathRef, NavigationPathRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SiteNavigationPathRef",
                    "type": SiteNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
