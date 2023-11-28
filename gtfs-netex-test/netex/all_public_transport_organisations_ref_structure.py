from dataclasses import dataclass
from netex.all_transport_organisations_ref_structure import AllTransportOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllPublicTransportOrganisationsRefStructure(AllTransportOrganisationsRefStructure):
    """
    Type for a reference to  all TRANSPORT ORGANISATIONs.
    """
