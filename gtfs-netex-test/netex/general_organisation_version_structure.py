from dataclasses import dataclass
from netex.other_organisation_version_structure import OtherOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralOrganisationVersionStructure(OtherOrganisationVersionStructure):
    """
    Type for an GENERAL ORGANISATION.
    """
    class Meta:
        name = "GeneralOrganisation_VersionStructure"
