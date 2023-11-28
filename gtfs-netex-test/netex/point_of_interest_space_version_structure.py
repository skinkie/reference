from dataclasses import dataclass, field
from typing import Optional
from netex.passage_type_enumeration import PassageTypeEnumeration
from netex.point_of_interest_component_version_structure import PointOfInterestComponentVersionStructure
from netex.point_of_interest_entrances_rel_structure import PointOfInterestEntrancesRelStructure
from netex.point_of_interest_space_ref_structure import PointOfInterestSpaceRefStructure
from netex.point_of_interest_space_type_enumeration import PointOfInterestSpaceTypeEnumeration
from netex.point_of_interest_space_version_structure_access_space_type import PointOfInterestSpaceVersionStructureAccessSpaceType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestSpaceVersionStructure(PointOfInterestComponentVersionStructure):
    """
    Type for a POINT OF INTEREST SPACE.

    :ivar access_space_type: Type of ACCESS SPACE.
    :ivar point_of_interest_space_type: Type of POINT OF INTEREST space.
    :ivar passage_type: Type of physical passage space.
    :ivar parent_point_of_interest_space_ref: if Space is a subzone of
        another POINT OF INTEREST SPACE identifies parent,
    :ivar entrances: Entrances to POINT OF INTEREST SPACE.
    """
    class Meta:
        name = "PointOfInterestSpace_VersionStructure"

    access_space_type: Optional[PointOfInterestSpaceVersionStructureAccessSpaceType] = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space_type: Optional[PointOfInterestSpaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passage_type: Optional[PassageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_point_of_interest_space_ref: Optional[PointOfInterestSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentPointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[PointOfInterestEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
