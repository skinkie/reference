from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.accessibility_assessment import AccessibilityAssessment
from netex.gender_limitation_enumeration import GenderLimitationEnumeration
from netex.passenger_equipment_version_structure import PassengerEquipmentVersionStructure
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SanitaryEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    """
    Type for a SANITARY FACILITY EQUIPMENT.

    :ivar accessibility_assessment:
    :ivar gender: Gender required to use facility.
    :ivar sanitary_facility_list:
    :ivar number_of_toilets: Number of Toilets
    :ivar free_to_use: Whether toilets are free to use.
    :ivar charge: Charge for using the facility.
    :ivar currency: Currency of Charge for using the facility.
    :ivar payment_methods: Methods of payment allowed.
    :ivar change_available: Whether chaneg is available. +v1.1
    :ivar wheelchair_turning_circle: Turning circle radius for a
        wheelchair.
    :ivar support_bar_height: Height of the support bar (when there is
        one). +v1.1
    :ivar call_button_available: Whether a call button is available.
        +v1.1
    :ivar sharps_disposal: Whether there is a facility for the disposal
        of sharps in toilet.
    :ivar staffing: Staffing of facility.
    :ivar locked_access: Whether toilet may be locked end thus a key is
        needed (or an equivalent tool) to access.+v1.1
    :ivar key_scheme: Key issuing scheme under which facility is
        accessible.
    """
    class Meta:
        name = "SanitaryEquipment_VersionStructure"

    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gender: Optional[GenderLimitationEnumeration] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_facility_list: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    number_of_toilets: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfToilets",
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
    charge: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    change_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    support_bar_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SupportBarHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    call_button_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CallButtonAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sharps_disposal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SharpsDisposal",
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
    locked_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LockedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    key_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyScheme",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
