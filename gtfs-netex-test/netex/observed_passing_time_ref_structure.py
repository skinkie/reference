from dataclasses import dataclass
from .passing_time_ref_structure import PassingTimeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTimeRefStructure(PassingTimeRefStructure):
    value: RestrictedVar
