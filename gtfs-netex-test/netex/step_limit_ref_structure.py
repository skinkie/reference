from dataclasses import dataclass

from .usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StepLimitRefStructure(UsageParameterRefStructure):
    pass
