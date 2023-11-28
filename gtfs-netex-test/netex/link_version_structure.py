from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.line_string import LineString
from netex.link_type_refs_rel_structure import LinkTypeRefsRelStructure
from netex.multilingual_string import MultilingualString
from netex.points_on_link_rel_structure import PointsOnLinkRelStructure
from netex.projections_rel_structure import ProjectionsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkVersionStructure(DataManagedObjectStructure):
    """
    Type for a LINK.

    :ivar name: Name of LINK.
    :ivar distance: Length of LINK.
    :ivar types: Types of LINK.
    :ivar line_string:
    :ivar projections: PROJECTIONs of the LINK.
    :ivar passing_through: POINTs through which LINK passes.
    """
    class Meta:
        name = "Link_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types: Optional[LinkTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passing_through: Optional[PointsOnLinkRelStructure] = field(
        default=None,
        metadata={
            "name": "passingThrough",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
