from dataclasses import dataclass

from .all_transport_organisations_ref_structure import AllTransportOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AllTransportOrganisationsRef(AllTransportOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
