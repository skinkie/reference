from dataclasses import dataclass
from netex.transport_organisation_ref_structure import TransportOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AuthorityRefStructure(TransportOrganisationRefStructure):
    """
    Type for a reference to an AUTHORITY.
    """
