from dataclasses import dataclass, field
from typing import List, Optional
from netex.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.berth_facility_enumeration import BerthFacilityEnumeration
from netex.class_of_use_ref import ClassOfUseRef
from netex.couchette_facility_enumeration import CouchetteFacilityEnumeration
from netex.fare_class_enumeration import FareClassEnumeration
from netex.gender_limitation_enumeration import GenderLimitationEnumeration
from netex.multilingual_string import MultilingualString
from netex.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from netex.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccommodationVersionedChildStructure(VersionedChildStructure):
    """
    Type for allowed combinations of ACCOMMODATION.

    :ivar name: Name of Accomodation _v1.1
    :ivar service_facility_set_ref:
    :ivar fare_class: Fare class of ACCOMMODATION.
    :ivar class_of_use_ref:
    :ivar accommodation_facility: Type of ACCOMMODATION. . Default is
        seating.
    :ivar couchette_facility: Type of Couchette.
    :ivar maximum_number_of_berths:
    :ivar berth_facility: Classification of BERTH FACILITY.
    :ivar shower_facility:
    :ivar toilet_facility: Toilet facilities for ACCOMMODATION.
    :ivar gender_limitation:
    :ivar nuisance_facility_list:
    :ivar passenger_comms_facility_list:
    """
    class Meta:
        name = "Accommodation_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set_ref: Optional[ServiceFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accommodation_facility: Optional[AccommodationFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    couchette_facility: Optional[CouchetteFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "CouchetteFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_berths: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfBerths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    berth_facility: Optional[BerthFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "BerthFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    shower_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ShowerFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    toilet_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ToiletFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gender_limitation: Optional[GenderLimitationEnumeration] = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    nuisance_facility_list: List[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "NuisanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    passenger_comms_facility_list: List[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCommsFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
