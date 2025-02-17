from dataclasses import dataclass, field
from typing import Union

from .luggage_spot_ref import LuggageSpotRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .passenger_spot_ref import PassengerSpotRef
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LocatableSpotRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "locatableSpotRefs_RelStructure"

    locatable_spot_ref: list[Union[LuggageSpotRef, PassengerVehicleSpotRef, PassengerSpotRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LuggageSpotRef",
                    "type": LuggageSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerVehicleSpotRef",
                    "type": PassengerVehicleSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpotRef",
                    "type": PassengerSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
