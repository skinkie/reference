from dataclasses import dataclass, field
from typing import Optional
from netex.authority_ref import AuthorityRef
from netex.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.levels_rel_structure import LevelsRelStructure
from netex.local_services_rel_structure import LocalServicesRelStructure
from netex.locale import Locale
from netex.management_agent_ref import ManagementAgentRef
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_derived_view_structure import OrganisationDerivedViewStructure
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.site_element_version_structure import SiteElementVersionStructure
from netex.site_entrances_rel_structure import SiteEntrancesRelStructure
from netex.site_ref_structure import SiteRefStructure
from netex.site_refs_rel_structure import SiteRefsRelStructure
from netex.site_type_enumeration import SiteTypeEnumeration
from netex.topographic_place_ref import TopographicPlaceRef
from netex.topographic_place_ref_structure import TopographicPlaceRefStructure
from netex.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from netex.topographic_place_view import TopographicPlaceView
from netex.travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteVersionStructure(SiteElementVersionStructure):
    """
    Type for an identified and data managed element making up a STOP PLACE.

    :ivar topographic_place_ref_or_topographic_place_view:
    :ivar additional_topographic_places: Additional Topographic Places
        in which SITE is located.
    :ivar site_type: Type of SITE.
    :ivar at_centre: Whether SITE is at centre of TOPOGRAPHIC PLACE.
    :ivar locale:
    :ivar choice:
    :ivar parent_site_ref: Reference to another SITE of which this SITE
        is deemed to be a subzone.
    :ivar adjacent_sites: Any references to another SITE of which this
        STOP PLACE is deemed to be a nearby but distinct.
    :ivar contained_in_place_ref: Most specific TOPOGRAPHIC PLACE within
        which the SITE lies. The TOPOGRAPHIC model can be used to
        determine what other places this also implies.
    :ivar levels: LEVELs found within SITe.
    :ivar entrances: Entrances to and within SITE.
    :ivar equipment_places: EQUIPMENT PLACEs within SITE COMPONENT.
    :ivar place_equipments: Items of fixed EQUIPMENT that may be located
        in places within the SITE  ELEMENT.
    :ivar local_services: LOCAL SERVICEs that may be located in PLACEs
        within the SITE ELEMENT.
    """
    class Meta:
        name = "Site_VersionStructure"

    topographic_place_ref_or_topographic_place_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    additional_topographic_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "additionalTopographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_type: Optional[SiteTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SiteType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    at_centre: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AtCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locale: Optional[Locale] = field(
        default=None,
        metadata={
            "name": "Locale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingOrganisationView",
                    "type": OrganisationDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    parent_site_ref: Optional[SiteRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjacent_sites: Optional[SiteRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "adjacentSites",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contained_in_place_ref: Optional[TopographicPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ContainedInPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    levels: Optional[LevelsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[SiteEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_places: Optional[EquipmentPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_equipments: Optional[PlaceEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_services: Optional[LocalServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
