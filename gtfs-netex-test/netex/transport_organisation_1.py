from dataclasses import dataclass

from .transport_organisation_version_structure import TransportOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransportOrganisation1(TransportOrganisationVersionStructure):
    class Meta:
        name = "TransportOrganisation"
        namespace = "http://www.netex.org.uk/netex"
