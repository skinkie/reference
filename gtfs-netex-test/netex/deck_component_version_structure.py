from dataclasses import dataclass, field
from typing import Optional

from .accessibility_assessment import AccessibilityAssessment
from .class_of_use_ref import ClassOfUseRef
from .deck_level_ref import DeckLevelRef
from .equipable_space_version_structure import EquipableSpaceVersionStructure
from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckComponentVersionStructure(EquipableSpaceVersionStructure):
    class Meta:
        name = "DeckComponent_VersionStructure"

    public_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_level_ref: Optional[DeckLevelRef] = field(
        default=None,
        metadata={
            "name": "DeckLevelRef",
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
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
