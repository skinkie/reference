from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.point_of_interest_ref import PointOfInterestRef
from netex.type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestDerivedViewStructure(DerivedViewStructure):
    """
    Type for POINT OF INTEREST VIEW.

    :ivar point_of_interest_ref:
    :ivar name: Name of POINT OF INTEREST.
    :ivar place_types: Classification of PLACE. Used for arbitrary
        documentation.
    :ivar short_name: Name of POINT OF INTEREST.
    """
    class Meta:
        name = "PointOfInterest_DerivedViewStructure"

    point_of_interest_ref: Optional[PointOfInterestRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_types: Optional[TypeOfPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
