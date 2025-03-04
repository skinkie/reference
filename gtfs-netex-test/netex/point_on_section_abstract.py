from dataclasses import dataclass

from .point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOnSectionAbstract(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "PointOnSection_"
        namespace = "http://www.netex.org.uk/netex"
