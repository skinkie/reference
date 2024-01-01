from dataclasses import dataclass
from .usage_parameter_ref_structure import UsageParameterRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingPolicyRefStructure(UsageParameterRefStructure):
    value: RestrictedVar
