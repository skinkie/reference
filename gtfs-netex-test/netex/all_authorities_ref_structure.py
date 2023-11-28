from dataclasses import dataclass
from netex.all_public_transport_organisations_ref_structure import AllPublicTransportOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllAuthoritiesRefStructure(AllPublicTransportOrganisationsRefStructure):
    """
    Type for a reference to  all AUTHORITIES.
    """
