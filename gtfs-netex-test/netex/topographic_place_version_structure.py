from dataclasses import dataclass, field
from typing import Optional
from netex.accesses_rel_structure import AccessesRelStructure
from netex.country_ref import CountryRef
from netex.country_refs_rel_structure import CountryRefsRelStructure
from netex.place_version_structure import PlaceVersionStructure
from netex.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.topographic_place_descriptors_rel_structure import TopographicPlaceDescriptorsRelStructure
from netex.topographic_place_ref_structure import TopographicPlaceRefStructure
from netex.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from netex.topographic_place_type_enumeration import TopographicPlaceTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicPlaceVersionStructure(PlaceVersionStructure):
    """
    Type for a TOPOGRAPHIC PLACE.

    :ivar iso_code: ISO 3166-2 code for subdivision of a country if
        relevant. E.g. GB-CAM.
    :ivar descriptor: Structured text descriptor of TOPOGRAPHIC PLACE.
    :ivar alternative_descriptors: Collection of aliases for the
        TOPOGRAPHIC PLACE.
    :ivar topographic_place_type: Classification of the TOPOGRAPHIC
        PLACE as a settlement. Enumerated value.
    :ivar place_centre: Whether the TOPOGRAPHIC PLACE is considered to
        be at the centre of a town. Default is false.
    :ivar post_code: Post code or partial post code associated with
        area. v1.1
    :ivar country_ref:
    :ivar other_countries: For TOPOGRAPHIC PLACEs thats span borders,
        references to additional  COUNTRY or COUNTRIEs  that place lies
        in.
    :ivar parent_topographic_place_ref: Parent TOPOGRAPHIC PLACE.
        Reference to another TOPOGRAPHIC PLACE that contains the child
        TOPOGRAPHIC PLACE completely. Must not be cyclic.
    :ivar adjacent_places: TOPOGRAPHIC PLACEs which are adjacent to the
        TOPOGRAPHIC PLACE. or which partially overlay. N.B. this should
        not be used for spatial containment. Instead the Parent Site
        should be used the TOPOGRAPHIC PLACE which completely contain
        the TOPOGRAPHIC PLACE, and on child TOPOGRAPHIC PLACEs for
        localities completely contained in the TOPOGRAPHIC PLACE.
    :ivar contained_in: TOPOGRAPHIC PLACEs other than then parent in
        which the place can be regarded as contained. a.
    :ivar accesses: ACCESS links to other PLACEs.
    """
    class Meta:
        name = "TopographicPlace_VersionStructure"

    iso_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IsoCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    descriptor: TopographicPlaceDescriptorVersionedChildStructure = field(
        metadata={
            "name": "Descriptor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    alternative_descriptors: Optional[TopographicPlaceDescriptorsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeDescriptors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_type: Optional[TopographicPlaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_centre: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlaceCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    post_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostCode",
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
    other_countries: Optional[CountryRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "otherCountries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_topographic_place_ref: Optional[TopographicPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentTopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjacent_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "adjacentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contained_in: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "containedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
