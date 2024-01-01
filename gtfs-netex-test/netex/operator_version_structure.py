from dataclasses import dataclass
from .transport_organisation_version_structure import (
    TransportOrganisationVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorVersionStructure(TransportOrganisationVersionStructure):
    class Meta:
        name = "Operator_VersionStructure"
