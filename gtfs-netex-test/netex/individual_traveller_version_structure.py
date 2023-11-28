from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.customer_ref import CustomerRef
from netex.gender_enumeration import GenderEnumeration
from netex.individual_passenger_infos_rel_structure import IndividualPassengerInfosRelStructure
from netex.multilingual_string import MultilingualString
from netex.vehicle_pooling_driver_infos_rel_structure import VehiclePoolingDriverInfosRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualTravellerVersionStructure(DataManagedObjectStructure):
    """
    Type for INDIVIDUAL TRAVELLER.

    :ivar name: Name of Traveller
    :ivar customer_ref:
    :ivar identity_verified: Whether traveller'ss identify has been
        verified. has been
    :ivar ranking: Rating for traveller
    :ivar gender: Gender of traveller.
    :ivar talkative: Whether traveller likes to talk.
    :ivar smoker: Whether traveller  likes to talk.
    :ivar languages: Languages spoken
    :ivar vehicle_pooling_driver_infos: VEHICLE POOLING DRIVER INFOrs
        for Traveller
    :ivar individual_passenger_infos: INDIVIDUAL PASSENGER INFOrs for
        Traveller
    """
    class Meta:
        name = "IndividualTraveller_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    identity_verified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IdentityVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gender: Optional[GenderEnumeration] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    talkative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Talkative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    smoker: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Smoker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    languages: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    vehicle_pooling_driver_infos: Optional[VehiclePoolingDriverInfosRelStructure] = field(
        default=None,
        metadata={
            "name": "vehiclePoolingDriverInfos",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    individual_passenger_infos: Optional[IndividualPassengerInfosRelStructure] = field(
        default=None,
        metadata={
            "name": "individualPassengerInfos",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
