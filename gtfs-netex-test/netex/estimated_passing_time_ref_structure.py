from dataclasses import dataclass

from .passing_time_ref_structure import PassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeRefStructure(PassingTimeRefStructure):
    pass
