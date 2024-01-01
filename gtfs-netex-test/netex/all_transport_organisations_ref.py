from dataclasses import dataclass
from .all_transport_organisations_ref_structure import (
    AllTransportOrganisationsRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllTransportOrganisationsRef(AllTransportOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
