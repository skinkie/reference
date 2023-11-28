from dataclasses import dataclass
from netex.online_service_operator_ref_structure import OnlineServiceOperatorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceOperatorRef(OnlineServiceOperatorRefStructure):
    """Reference to an ONLINE SERVICE OPERATOR.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
