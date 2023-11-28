from dataclasses import dataclass, field
from typing import List, Optional
from netex.access_facility_enumeration import AccessFacilityEnumeration
from netex.emergency_service_enumeration import EmergencyServiceEnumeration
from netex.facility_set_version_structure import FacilitySetVersionStructure
from netex.hire_facility_enumeration import HireFacilityEnumeration
from netex.luggage_locker_facility_enumeration import LuggageLockerFacilityEnumeration
from netex.luggage_service_facility_enumeration import LuggageServiceFacilityEnumeration
from netex.money_facility_enumeration import MoneyFacilityEnumeration
from netex.parking_facility_enumeration import ParkingFacilityEnumeration
from netex.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteFacilitySetStructure(FacilitySetVersionStructure):
    """
    Type for a SITEFACILITY.

    :ivar access_facility_list: List of ACCESS FACILITies. + v1.1
    :ivar emergency_service_list: List of EMERGENCY SERVICE FACILITies.
    :ivar hire_facility_list: List of HIRE FACILITies.
    :ivar luggage_locker_facility_list: List of LUGGAGE LOCKER
        FACILITies.
    :ivar luggage_service_facility_list: List of LUGGAGE SERVICE
        FACILITies.
    :ivar money_facility_list: List of MONEY FACILITies.
    :ivar parking_facility_list: List of PARKING FACILITies.
    :ivar staffing: Classification of STAFFING.
    """
    access_facility_list: List[AccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    emergency_service_list: List[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "EmergencyServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    hire_facility_list: List[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HireFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    luggage_locker_facility_list: List[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LuggageLockerFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    luggage_service_facility_list: List[LuggageServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LuggageServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    money_facility_list: List[MoneyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MoneyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    parking_facility_list: List[ParkingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    staffing: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
