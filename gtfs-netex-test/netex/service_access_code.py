from dataclasses import dataclass, field
from netex.service_access_code_version_structure import ServiceAccessCodeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceAccessCode(ServiceAccessCodeVersionStructure):
    """Code to access a service, can be numerical code, barcode, flashcode, etc.

    +V1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
