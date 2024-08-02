from dataclasses import dataclass, field
from typing import Optional, Union

from .access_facility import AccessFacility
from .accommodation_facility import AccommodationFacility
from .assistance_facility import AssistanceFacility
from .fare_class_facility import FareClassFacility
from .hire_facility import HireFacility
from .luggage_facility import LuggageFacility
from .mobility_facility import MobilityFacility
from .nuisance_facility import NuisanceFacility
from .parking_facility import ParkingFacility
from .passenger_comms_facility import PassengerCommsFacility
from .passenger_information_facility import PassengerInformationFacility
from .refreshment_facility import RefreshmentFacility
from .reserved_space_facility import ReservedSpaceFacility
from .retail_facility import RetailFacility
from .sanitary_facility import SanitaryFacility
from .ticketing_facility import TicketingFacility

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AllFacilitiesFeatureStructure:
    choice: Optional[
        Union[
            AccessFacility,
            AccommodationFacility,
            AssistanceFacility,
            FareClassFacility,
            HireFacility,
            LuggageFacility,
            MobilityFacility,
            NuisanceFacility,
            ParkingFacility,
            PassengerCommsFacility,
            PassengerInformationFacility,
            RefreshmentFacility,
            ReservedSpaceFacility,
            RetailFacility,
            SanitaryFacility,
            TicketingFacility,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessFacility",
                    "type": AccessFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AccommodationFacility",
                    "type": AccommodationFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AssistanceFacility",
                    "type": AssistanceFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FareClassFacility",
                    "type": FareClassFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "HireFacility",
                    "type": HireFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "LuggageFacility",
                    "type": LuggageFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "MobilityFacility",
                    "type": MobilityFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "NuisanceFacility",
                    "type": NuisanceFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ParkingFacility",
                    "type": ParkingFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "PassengerCommsFacility",
                    "type": PassengerCommsFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "PassengerInformationFacility",
                    "type": PassengerInformationFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "RefreshmentFacility",
                    "type": RefreshmentFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ReservedSpaceFacility",
                    "type": ReservedSpaceFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "RetailFacility",
                    "type": RetailFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SanitaryFacility",
                    "type": SanitaryFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TicketingFacility",
                    "type": TicketingFacility,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
