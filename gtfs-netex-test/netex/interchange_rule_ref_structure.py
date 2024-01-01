from dataclasses import dataclass
from .interchange_ref_structure import InterchangeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleRefStructure(InterchangeRefStructure):
    value: RestrictedVar
