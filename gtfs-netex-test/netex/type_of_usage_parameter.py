from dataclasses import dataclass

from .type_of_usage_parameter_version_structure import TypeOfUsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfUsageParameter(TypeOfUsageParameterVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
