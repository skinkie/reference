from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.boarding_permission_enumeration import BoardingPermissionEnumeration
from netex.class_of_use_ref import ClassOfUseRef
from netex.fare_class_enumeration import FareClassEnumeration
from netex.multilingual_string import MultilingualString
from netex.service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnboardStayVersionedChlldStructure(VersionedChildStructure):
    """
    Type for allowed combinations of boarding permission.

    :ivar name: Name of ON BOARD STay +v1.1
    :ivar service_facility_set_ref:
    :ivar fare_class: Fare class of Boarding permission.
    :ivar class_of_use_ref:
    :ivar boarding_permission: Type of Accommodation . Default is
        seating.
    :ivar period: Period allowed for boarding/ alighting before journey
        start /end.
    """
    class Meta:
        name = "OnboardStay_VersionedChlldStructure"

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
    boarding_permission: Optional[BoardingPermissionEnumeration] = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
