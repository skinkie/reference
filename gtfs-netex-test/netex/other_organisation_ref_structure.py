from dataclasses import dataclass
from netex.organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OtherOrganisationRefStructure(OrganisationRefStructure):
    """
    Type for a reference to an OTHER ORGANISATION.
    """
