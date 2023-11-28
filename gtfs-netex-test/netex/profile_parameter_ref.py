from dataclasses import dataclass
from netex.usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ProfileParameterRef(UsageParameterRefStructure):
    """
    Reference to a PROFILE usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
