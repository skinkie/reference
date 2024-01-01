from dataclasses import dataclass
from .journey_timing_ref_structure import JourneyTimingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleTimingRefStructure(JourneyTimingRefStructure):
    value: RestrictedVar
