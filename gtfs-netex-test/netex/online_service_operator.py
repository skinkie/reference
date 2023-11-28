from dataclasses import dataclass, field
from netex.online_service_operator_version_structure import OnlineServiceOperatorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceOperator(OnlineServiceOperatorVersionStructure):
    """An organisation that provides online access to an ONLINE SERVICE without
    operating transportation services of travellers.

    +v1.2.2

    :ivar id: Identifier of ONLINE SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
