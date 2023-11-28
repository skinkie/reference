from dataclasses import dataclass
from netex.organisation_part_ref_structure import OrganisationPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationPartRef(OrganisationPartRefStructure):
    """
    Reference to an ORGANISATION PART.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
