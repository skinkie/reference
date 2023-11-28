from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.local_service_version_structure import LocalServiceVersionStructure
from netex.luggage_service_facility_enumeration import LuggageServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for LUGGAGE SERVICE.

    :ivar luggage_service_facility_list: LUGGAGE SERVICEs available.
    :ivar luggage_trolleys: Whether there are trolleys.
    :ivar wheelchair_luggage_trolleys: Whether there are wheel chair
        trolleys.
    :ivar free_to_use: Whether the service is free to use.
    :ivar maximum_bag_width: Maximum width of luggage accepted by
        service.
    :ivar maximum_bag_height: Maximum height of luggage accepted by
        service.
    :ivar maximum_bag_depth: Maximum depth of luggage accepted by
        service.
    :ivar maximum_bag_weight: Maximum weight of the luggage. +v1.1
    :ivar luggage_maximal_weigth: Maximum weight of the luggage (in
        kilograms).
    """
    class Meta:
        name = "LuggageService_VersionStructure"

    luggage_service_facility_list: List[LuggageServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LuggageServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    luggage_trolleys: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LuggageTrolleys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_luggage_trolleys: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairLuggageTrolleys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    free_to_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeToUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_maximal_weigth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LuggageMaximalWeigth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
