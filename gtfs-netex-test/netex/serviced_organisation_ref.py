from dataclasses import dataclass
from .serviced_organisation_ref_structure import (
    ServicedOrganisationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicedOrganisationRef(ServicedOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
