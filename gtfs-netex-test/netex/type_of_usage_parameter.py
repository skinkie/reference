from dataclasses import dataclass, field
from netex.type_of_usage_parameter_version_structure import TypeOfUsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfUsageParameter(TypeOfUsageParameterVersionStructure):
    """
    Category of USAGE PARAMETER user.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
