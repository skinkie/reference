from dataclasses import dataclass

from .organisation_version_structure import OrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransportOrganisation2(OrganisationVersionStructure):
    class Meta:
        name = "TransportOrganisation_"
        namespace = "http://www.netex.org.uk/netex"
