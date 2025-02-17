from dataclasses import dataclass, field
from typing import Optional

from .access_feature_enumeration import AccessFeatureEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessSummaryVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AccessSummary_VersionedChildStructure"

    access_feature_type: AccessFeatureEnumeration = field(
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    count: int = field(
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
