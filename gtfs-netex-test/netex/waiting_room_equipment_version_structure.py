from dataclasses import dataclass, field
from typing import List, Optional
from netex.class_of_use_ref import ClassOfUseRef
from netex.fare_class_enumeration import FareClassEnumeration
from netex.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.waiting_equipment_version_structure import WaitingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WaitingRoomEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    """
    Type for a Waiting Room EQUIPMENT.

    :ivar fare_class: Class of fare needed to use waiting room.
    :ivar women_only: Whether waiting room is only for women.
    :ivar sanitary: Sanitary facility.
    :ivar class_of_use_ref:
    """
    class Meta:
        name = "WaitingRoomEquipment_VersionStructure"

    fare_class: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    women_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WomenOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Sanitary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
