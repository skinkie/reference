from dataclasses import dataclass
from netex.general_organisation_ref_structure import GeneralOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralOrganisationRef(GeneralOrganisationRefStructure):
    """
    Reference to a GENERAL ORGANISATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
