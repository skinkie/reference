from dataclasses import dataclass, field
from typing import Optional
from netex.covered_enumeration import CoveredEnumeration
from netex.gated_enumeration import GatedEnumeration
from netex.lighting_enumeration import LightingEnumeration
from netex.multilingual_string import MultilingualString
from netex.point_version_structure import PointVersionStructure
from netex.presentation_structure import PresentationStructure
from netex.public_use_enumeration import PublicUseEnumeration
from netex.site_component_ref_structure import SiteComponentRefStructure
from netex.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathJunctionVersionStructure(PointVersionStructure):
    """
    Type for a PATH LINK VIEW.

    :ivar parent_zone_ref: Parent ZONE that contains this PATH JUNCTION.
    :ivar public_use: Whether the component is available for public use
        or is restricted.
    :ivar covered: Whether the component is Indoors or outdoors. Default
        is Indoors.
    :ivar gated: Whether the component is within a gated area or freely
        accessible without a pass or ticket.
    :ivar lighting: Whether the component is lit or not. Default is well
        Lit.
    :ivar all_areas_wheelchair_accessible: Whether all areas of the
        component are wheelchair accessible.
    :ivar person_capacity: Total number of people that component can
        contain.
    :ivar presentation: Presentation defaults for SITE ELEMENT. +V1.2.2
    :ivar facilities: Facilities available at SITe.
    :ivar label: Additional Label of PATH JUNCTION.
    :ivar site_component_ref: PATH JUNCTION is within the referenced
        SITE COMPONENT.
    """
    class Meta:
        name = "PathJunction_VersionStructure"

    parent_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[SiteFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_component_ref: Optional[SiteComponentRefStructure] = field(
        default=None,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
