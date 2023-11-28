from dataclasses import dataclass
from netex.organisation_derived_view_structure import OrganisationDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationView(OrganisationDerivedViewStructure):
    """Simplified view of ORGANISATION.

    All data except the identifier will be derived through the
    referenced to the Organisation.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
