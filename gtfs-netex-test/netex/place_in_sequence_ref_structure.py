from dataclasses import dataclass

from .point_in_sequence_ref_structure import PointInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlaceInSequenceRefStructure(PointInSequenceRefStructure):
    pass
