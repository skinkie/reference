from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .boarding_permission import BoardingPermission
from .class_of_use_ref import ClassOfUseRef
from .entity_in_version_structure import VersionedChildStructure
from .fare_class import FareClass
from .multilingual_string import MultilingualString
from .restricted_service_facility_set_ref import RestrictedServiceFacilitySetRef
from .service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OnboardStayVersionedChlldStructure(VersionedChildStructure):
    class Meta:
        name = "OnboardStay_VersionedChlldStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set_ref: Optional[Union[RestrictedServiceFacilitySetRef, ServiceFacilitySetRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RestrictedServiceFacilitySetRef",
                    "type": RestrictedServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fare_class: Optional[FareClass] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_permission: Optional[BoardingPermission] = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
