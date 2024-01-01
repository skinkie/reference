from dataclasses import dataclass
from .point_in_sequence_ref_structure import PointInSequenceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointInJourneyPatternRefStructure(PointInSequenceRefStructure):
    value: RestrictedVar
