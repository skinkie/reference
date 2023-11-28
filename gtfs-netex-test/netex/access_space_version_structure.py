from dataclasses import dataclass, field
from typing import Optional
from netex.access_space_ref_structure import AccessSpaceRefStructure
from netex.access_space_type_enumeration import AccessSpaceTypeEnumeration
from netex.passage_type_enumeration import PassageTypeEnumeration
from netex.stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessSpaceVersionStructure(StopPlaceSpaceVersionStructure):
    """
    Type for an ACCESS SPACE.

    :ivar access_space_type: Type of ACCESS SPACE.
    :ivar passage_type: Type of passage associated with ACCESS SPACE.
    :ivar parent_access_space_ref: if ACCESS SPACE is a subzone of
        another ACCESS SPACE identifies parent,
    """
    class Meta:
        name = "AccessSpace_VersionStructure"

    access_space_type: Optional[AccessSpaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
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
    parent_access_space_ref: Optional[AccessSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentAccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
