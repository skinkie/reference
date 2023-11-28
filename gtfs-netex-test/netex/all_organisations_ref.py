from dataclasses import dataclass
from netex.all_organisations_ref_structure import AllOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllOrganisationsRef(AllOrganisationsRefStructure):
    """
    Reference to all ORGANISATIONs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
