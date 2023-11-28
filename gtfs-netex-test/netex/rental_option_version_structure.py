from dataclasses import dataclass
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalOptionVersionStructure(UsageParameterVersionStructure):
    """
    Type for RENTAL OPTION.
    """
    class Meta:
        name = "RentalOption_VersionStructure"
