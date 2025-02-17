from dataclasses import dataclass

from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RentalOptionVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "RentalOption_VersionStructure"
