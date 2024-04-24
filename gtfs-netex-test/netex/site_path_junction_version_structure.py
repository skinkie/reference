from dataclasses import dataclass, field
from typing import Optional

from .covered_enumeration import CoveredEnumeration
from .gated_enumeration import GatedEnumeration
from .generic_path_junction_version_structure import GenericPathJunctionVersionStructure
from .lighting_enumeration import LightingEnumeration
from .multilingual_string import MultilingualString
from .place_equipments_rel_structure import PlaceEquipmentsRelStructure
from .presentation_structure import PresentationStructure
from .public_use_enumeration import PublicUseEnumeration
from .site_component_ref_structure import SiteComponentRefStructure
from .site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathJunctionVersionStructure(GenericPathJunctionVersionStructure):
    class Meta:
        name = "SitePathJunction_VersionStructure"

    parent_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[SiteFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    site_component_ref: Optional[SiteComponentRefStructure] = field(
        default=None,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_equipments: Optional[PlaceEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
