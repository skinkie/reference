from dataclasses import dataclass

from .all_organisations_ref_structure import AllOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AllOrganisationsRef(AllOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
