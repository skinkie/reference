from dataclasses import dataclass
from netex.all_organisations_ref_structure import AllOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllTransportOrganisationsRefStructure(AllOrganisationsRefStructure):
    """
    Type for a reference to  all TRANSPORT ORGANISATIONs.
    """
