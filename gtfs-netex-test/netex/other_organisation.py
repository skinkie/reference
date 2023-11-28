from dataclasses import dataclass
from netex.other_organisation_version_structure import OtherOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OtherOrganisation(OtherOrganisationVersionStructure):
    """
    Generic ORGANISATION being neither an AUTHORITY, neither a public transport
    OPERATOR (TRAVEL AGENT, MANAGEMENT AGENT, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
