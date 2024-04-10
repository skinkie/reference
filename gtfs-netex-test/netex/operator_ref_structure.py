from dataclasses import dataclass

from .transport_organisation_ref_structure import TransportOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorRefStructure(TransportOrganisationRefStructure):
    pass
