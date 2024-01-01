from dataclasses import dataclass
from .transport_organisation_ref_structure import (
    TransportOrganisationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorRefStructure(TransportOrganisationRefStructure):
    value: RestrictedVar
