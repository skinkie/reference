from dataclasses import dataclass, field
from typing import Optional
from netex.accesses_in_frame_rel_structure import AccessesInFrameRelStructure
from netex.addresses_in_frame_rel_structure import AddressesInFrameRelStructure
from netex.check_constraint_delays_in_frame_rel_structure import CheckConstraintDelaysInFrameRelStructure
from netex.check_constraint_in_frame_rel_structure import CheckConstraintInFrameRelStructure
from netex.check_constraint_throughputs_in_frame_rel_structure import CheckConstraintThroughputsInFrameRelStructure
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.countries_in_frame_rel_structure import CountriesInFrameRelStructure
from netex.flexible_stop_places_in_frame_rel_structure import FlexibleStopPlacesInFrameRelStructure
from netex.groups_of_stop_places_in_frame_rel_structure import GroupsOfStopPlacesInFrameRelStructure
from netex.navigation_paths_in_frame_rel_structure import NavigationPathsInFrameRelStructure
from netex.parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from netex.path_junctions_in_frame_rel_structure import PathJunctionsInFrameRelStructure
from netex.path_links_in_frame_rel_structure import PathLinksInFrameRelStructure
from netex.point_of_interest_classification_hierarchies_in_frame_rel_structure import PointOfInterestClassificationHierarchiesInFrameRelStructure
from netex.point_of_interest_classifications_in_frame_rel_structure import PointOfInterestClassificationsInFrameRelStructure
from netex.points_of_interest_in_frame_rel_structure import PointsOfInterestInFrameRelStructure
from netex.site_facility_sets_in_frame_rel_structure import SiteFacilitySetsInFrameRelStructure
from netex.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a SITE FRAME.

    :ivar countries: COUNTRIES in Frame
    :ivar topographic_places: PLACEs in frame.
    :ivar addresses: ADDRESSes in frame.
    :ivar accesses: ACCESS links in frame.
    :ivar groups_of_stop_places: GROUPS of STOP PLACEs in frame.
    :ivar stop_places: STOP PLACEs in frame.
    :ivar flexible_stop_places: STOP PLACEs in frame.
    :ivar points_of_interest: POINTS OF INTEREST in frame.
    :ivar parkings: PARKINGs in frame.
    :ivar navigation_paths: NAVIGATION PATHs in frame.
    :ivar path_links: PATH LINKs in frame.
    :ivar path_junctions: PATH JUNCTIONs in frame.
    :ivar check_constraints: CHECK CONSTRAINTs in frame.
    :ivar check_constraint_delays: CHECK CONSTRAINTs DELAYs in frame.
    :ivar check_constraint_throughputs: CHECK CONSTRAINTs DELAYs in
        frame.
    :ivar point_of_interest_classifications: POINT OF INTEREST
        CLASSIFICATIONS in frame.
    :ivar point_of_interest_classification_hierarchies: POINT OF
        INTEREST CLASSIFICATION HIERARCHies in frame.
    :ivar tariff_zones: TARIFF ZONEs in frame.
    :ivar site_facility_sets:
    """
    class Meta:
        name = "Site_VersionFrameStructure"

    countries: Optional[CountriesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_places: Optional[TopographicPlacesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "topographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    addresses: Optional[AddressesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accesses: Optional[AccessesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_stop_places: Optional[GroupsOfStopPlacesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfStopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_places: Optional[StopPlacesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "stopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_places: Optional[FlexibleStopPlacesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "flexibleStopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_of_interest: Optional[PointsOfInterestInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parkings: Optional[ParkingsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_paths: Optional[NavigationPathsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_links: Optional[PathLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junctions: Optional[PathJunctionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraints: Optional[CheckConstraintInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint_delays: Optional[CheckConstraintDelaysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraintDelays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint_throughputs: Optional[CheckConstraintThroughputsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraintThroughputs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_classifications: Optional[PointOfInterestClassificationsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "pointOfInterestClassifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_classification_hierarchies: Optional[PointOfInterestClassificationHierarchiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "pointOfInterestClassificationHierarchies",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zones: Optional[TariffZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_facility_sets: Optional[SiteFacilitySetsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "siteFacilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
