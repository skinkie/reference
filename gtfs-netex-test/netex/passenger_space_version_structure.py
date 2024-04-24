from dataclasses import dataclass, field
from typing import Optional

from .deck_space_version_structure import DeckSpaceVersionStructure
from .luggage_spots_rel_structure import LuggageSpotsRelStructure
from .passenger_spots_rel_structure import PassengerSpotsRelStructure
from .passenger_vehicle_spots_rel_structure import PassengerVehicleSpotsRelStructure
from .spot_affinities_rel_structure import SpotAffinitiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpaceVersionStructure(DeckSpaceVersionStructure):
    class Meta:
        name = "PassengerSpace_VersionStructure"

    standing_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StandingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_spots: Optional[PassengerSpotsRelStructure] = field(
        default=None,
        metadata={
            "name": "passengerSpots",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_spots: Optional[LuggageSpotsRelStructure] = field(
        default=None,
        metadata={
            "name": "luggageSpots",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_vehicle_spots: Optional[PassengerVehicleSpotsRelStructure] = field(
        default=None,
        metadata={
            "name": "passengerVehicleSpots",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spot_affinities: Optional[SpotAffinitiesRelStructure] = field(
        default=None,
        metadata={
            "name": "spotAffinities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
