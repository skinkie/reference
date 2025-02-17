from dataclasses import dataclass

from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class UsageParameter1(UsageParameterVersionStructure):
    class Meta:
        name = "UsageParameter"
        namespace = "http://www.netex.org.uk/netex"
