from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.individual_traveller_ref import IndividualTravellerRef
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualPassengerInfoVersionStructure(DataManagedObjectStructure):
    """
    Type for INDIVIDUAL PASSENGER INFO.

    :ivar individual_traveller_ref:
    :ivar ranking: Rating for driver.
    :ivar last_trip_date: Date of last trip.
    :ivar comments_about: Comments on passenger.
    :ivar travelling_with_pet: Whether  travelling with Pet.
    """
    class Meta:
        name = "IndividualPassengerInfo_VersionStructure"

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
