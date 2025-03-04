from dataclasses import dataclass, field
from typing import Optional

from .passage_type_enumeration import PassageTypeEnumeration
from .point_of_interest_component_version_structure import PointOfInterestComponentVersionStructure
from .point_of_interest_entrances_rel_structure import PointOfInterestEntrancesRelStructure
from .point_of_interest_space_ref_structure import PointOfInterestSpaceRefStructure
from .point_of_interest_space_type_enumeration import PointOfInterestSpaceTypeEnumeration
from .point_of_interest_space_version_structure_access_space_type import PointOfInterestSpaceVersionStructureAccessSpaceType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestSpaceVersionStructure(PointOfInterestComponentVersionStructure):
    class Meta:
        name = "PointOfInterestSpace_VersionStructure"

    access_space_type: Optional[PointOfInterestSpaceVersionStructureAccessSpaceType] = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_of_interest_space_type: Optional[PointOfInterestSpaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: Optional[PassageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_point_of_interest_space_ref: Optional[PointOfInterestSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentPointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrances: Optional[PointOfInterestEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
