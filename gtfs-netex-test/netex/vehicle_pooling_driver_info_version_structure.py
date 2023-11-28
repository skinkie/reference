from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.driving_style_enumeration import DrivingStyleEnumeration
from netex.individual_traveller_ref import IndividualTravellerRef
from netex.multilingual_string import MultilingualString
from netex.vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingDriverInfoVersionStructure(DataManagedObjectStructure):
    """
    Type for VEHICLE POOLING DRIVER INFO.

    :ivar individual_traveller_ref:
    :ivar ranking: Rating for driver.
    :ivar last_trip_date: Date of last trip.
    :ivar comments_about: Comments on driver.
    :ivar travelling_with_pet: Whether driver has pet.
    :ivar driving_licence_verified: Whether driving licence has been
        verified.
    :ivar insurance_verified: Whether insurance has been verified.
    :ivar driving_style: Preferrred style of driving.
    :ivar number_of_proposed_trips: Number of trips proposed
    :ivar number_of_travellers_carried: Number of travellers carried
    :ivar vehicle_ref:
    """
    class Meta:
        name = "VehiclePoolingDriverInfo_VersionStructure"

    individual_traveller_ref: Optional[IndividualTravellerRef] = field(
        default=None,
        metadata={
            "name": "IndividualTravellerRef",
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
    last_trip_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastTripDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    comments_about: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CommentsAbout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travelling_with_pet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TravellingWithPet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driving_licence_verified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DrivingLicenceVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    insurance_verified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InsuranceVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driving_style: Optional[DrivingStyleEnumeration] = field(
        default=None,
        metadata={
            "name": "DrivingStyle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_proposed_trips: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfProposedTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_travellers_carried: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTravellersCarried",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
