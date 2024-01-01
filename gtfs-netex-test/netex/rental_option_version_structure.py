from dataclasses import dataclass
from .usage_parameter_version_structure import UsageParameterVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RentalOptionVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "RentalOption_VersionStructure"
