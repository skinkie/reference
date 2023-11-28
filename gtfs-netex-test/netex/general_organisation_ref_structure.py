from dataclasses import dataclass
from netex.other_organisation_ref_structure import OtherOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralOrganisationRefStructure(OtherOrganisationRefStructure):
    """
    Type for a reference to a GENERAL ORGANISATION.
    """
