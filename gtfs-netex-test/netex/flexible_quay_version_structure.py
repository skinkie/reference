from dataclasses import dataclass, field
from typing import Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.flexible_stop_place_ref import FlexibleStopPlaceRef
from netex.multilingual_string import MultilingualString
from netex.place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleQuayVersionStructure(PlaceVersionStructure):
    """
    Type for FLEXIBLE QUAY.

    :ivar name_suffix: Further suffix to name that may be used in some
        contexts.
    :ivar alternative_names: Alternative names.
    :ivar flexible_stop_place_ref:
    :ivar transport_mode: Primary MODE of Vehicle transport.
    :ivar boarding_use: Whether space can be used for boarding or en
        route to boarding. Default is true.
    :ivar alighting_use: Whether space can be used for alighting or en
        route to boarding. Default is true.
    :ivar public_code: Public identifier code of FLEXIBLE QUAY.
    """
    class Meta:
        name = "FlexibleQuay_VersionStructure"

    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_place_ref: Optional[FlexibleStopPlaceRef] = field(
        default=None,
        metadata={
            "name": "FlexibleStopPlaceRef",
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
    boarding_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alighting_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingUse",
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
