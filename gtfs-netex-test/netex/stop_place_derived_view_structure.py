from dataclasses import dataclass, field
from typing import Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.derived_view_structure import DerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.stop_place_ref import StopPlaceRef
from netex.stop_type_enumeration import StopTypeEnumeration
from netex.taxi_rank_ref import TaxiRankRef
from netex.type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceDerivedViewStructure(DerivedViewStructure):
    """
    Type for STOP PLACE VIEW.

    :ivar taxi_rank_ref_or_stop_place_ref:
    :ivar name: Name of STOP PLACE.
    :ivar place_types: Classification of PLACE.
    :ivar short_name: Name of STOP PLACE.
    :ivar public_code: Short public code for passengers to use when
        uniquely identifying the stop by SMS and other self-service
        channels.
    :ivar stop_place_type: Type of STOP PLACE.
    :ivar transport_mode: Primary MODE of Vehicle transport.
    """
    class Meta:
        name = "StopPlace_DerivedViewStructure"

    taxi_rank_ref_or_stop_place_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
