from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.group_membership_refs_rel_structure import GroupMembershipRefsRelStructure
from netex.location_structure_2 import LocationStructure2
from netex.multilingual_string import MultilingualString
from netex.projections_rel_structure import ProjectionsRelStructure
from netex.type_of_point_refs_rel_structure import TypeOfPointRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointVersionStructure(DataManagedObjectStructure):
    """
    Type for a POINT.

    :ivar name: Name of POINT.
    :ivar location: The position of a POINT with a reference to a given
        LOCATING SYSTEM (e. g. coordinates).
    :ivar point_number: Arbitrary alternative identifier for the POINT.
    :ivar types: Types of POINT. Used for arbitrary documentation -
        Specific types of POINTs and LINKs such as ROUTE POINT, TIMING
        POINT, etc are also proper subtypes of POINT.
    :ivar projections: PROJECTIONs of POINT onto another ENTITY or
        layer.
    :ivar group_memberships: GROUPs OF POINTs to which POINT belongs.
    """
    class Meta:
        name = "Point_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PointNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types: Optional[TypeOfPointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_memberships: Optional[GroupMembershipRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupMemberships",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
