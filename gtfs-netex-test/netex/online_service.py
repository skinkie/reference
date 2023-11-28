from dataclasses import dataclass, field
from netex.online_service_version_structure import OnlineServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineService(OnlineServiceVersionStructure):
    """Any remotely accessible service providing access to any mode of
    transportation and/or information related to transportation services.

    +v1.2.2

    :ivar id: Identifier of an ONLINE SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
