from dataclasses import dataclass, field
from netex.service_access_right_version_structure import ServiceAccessRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceAccessRight1(ServiceAccessRightVersionStructure):
    """
    An immaterial marketable element dedicated to accessing some services.
    """
    class Meta:
        name = "ServiceAccessRight"
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
