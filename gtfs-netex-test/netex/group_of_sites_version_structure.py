from dataclasses import dataclass, field
from typing import Optional

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .external_object_ref_structure import ExternalObjectRefStructure
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .polygon import Polygon
from .projections_rel_structure import ProjectionsRelStructure
from .simple_point_version_structure import SimplePointVersionStructure
from .site_refs_rel_structure import SiteRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSitesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfSites_VersionStructure"

    centroid: Optional[SimplePointVersionStructure] = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[SiteRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
