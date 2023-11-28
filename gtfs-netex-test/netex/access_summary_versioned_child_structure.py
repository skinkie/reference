from dataclasses import dataclass, field
from typing import Optional
from netex.access_feature_enumeration import AccessFeatureEnumeration
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessSummaryVersionedChildStructure(VersionedChildStructure):
    """
    Type for ACCESS SUMMARY.

    :ivar access_feature_type: Type of access feature, e.g. lift,
        stairs,
    :ivar count: Count of feature, e.g. number of lifts, stairs.
    :ivar transition: Nature of access feature transition e.g. up or
        down.
    """
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
        }
    )
