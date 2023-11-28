from dataclasses import dataclass, field
from netex.serviced_organisation_version_structure import ServicedOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServicedOrganisation(ServicedOrganisationVersionStructure):
    """
    ORGANISATION for which Service is provided, e.g. school college.

    :ivar id: Identifier of  SERVICED ORGANISATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
