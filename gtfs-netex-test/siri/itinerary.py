from dataclasses import dataclass, field
from typing import List, Optional

from .destination_abstract import DestinationAbstract
from .extension_type import ExtensionType
from .group_of_locations import GroupOfLocations
from .location import Location

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Itinerary(GroupOfLocations):
    location_contained_in_itinerary: List["Itinerary.LocationContainedInItinerary"] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInItinerary",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    route_destination: List[DestinationAbstract] = field(
        default_factory=list,
        metadata={
            "name": "routeDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )

    @dataclass(kw_only=True)
    class LocationContainedInItinerary(Location):
        index: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
