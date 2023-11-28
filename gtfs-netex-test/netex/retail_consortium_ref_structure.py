from dataclasses import dataclass
from netex.organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailConsortiumRefStructure(OrganisationRefStructure):
    """
    Type for Reference to a RETAIL CONSORTIUM.
    """
