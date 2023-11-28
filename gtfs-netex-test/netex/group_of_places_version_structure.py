from dataclasses import dataclass, field
from typing import Optional
from netex.country_ref import CountryRef
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.place_ref_structure import PlaceRefStructure
from netex.place_refs_rel_structure import PlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfPlacesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF PLACES.

    :ivar members: PLACEs in GROUP OF PLACEs.
    :ivar country_ref:
    :ivar main_place_ref: Primary PLACE in GROUP OF PLACEs, if relevant.
    """
    class Meta:
        name = "GroupOfPlaces_VersionStructure"

    members: Optional[PlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    main_place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
