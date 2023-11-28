from dataclasses import dataclass, field
from typing import List, Optional
from netex.accessibility_tool_enumeration import AccessibilityToolEnumeration
from netex.assistance_availability_enumeration import AssistanceAvailabilityEnumeration
from netex.assistance_facility_enumeration import AssistanceFacilityEnumeration
from netex.emergency_service_enumeration import EmergencyServiceEnumeration
from netex.local_service_version_structure import LocalServiceVersionStructure
from netex.safety_facility_enumeration import SafetyFacilityEnumeration
from netex.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for an ASSISTANCE SERVICE.

    :ivar assistance_facility_list:
    :ivar assistance_availability: Availability of assistance service.
    :ivar staffing: Staffing service.
    :ivar accessibility_tool_list:
    :ivar languages: Languages spoken for assistance.
    :ivar accessibility_trained_staff: Whether staff are accessibility
        trained.
    :ivar emergency_service_list: Emergency service assistance
        available.
    :ivar safety_facility_list: Safety facilities.
    """
    class Meta:
        name = "AssistanceService_VersionStructure"

    assistance_facility_list: List[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    assistance_availability: Optional[AssistanceAvailabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistanceAvailability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    accessibility_tool_list: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
    accessibility_trained_staff: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessibilityTrainedStaff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    safety_facility_list: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
