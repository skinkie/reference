from dataclasses import dataclass

from .interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InterchangeRuleRefStructure(InterchangeRefStructure):
    pass
