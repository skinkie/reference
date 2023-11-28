from dataclasses import dataclass, field
from netex.service_site_version_structure import ServiceSiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceSite(ServiceSiteVersionStructure):
    """
    A sub-type of SITE which is of specific interest for the operator (e.g. where a
    joint service or a joint fee is proposed).

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
