from dataclasses import dataclass

from .other_organisation_ref_structure import OtherOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelAgentRefStructure(OtherOrganisationRefStructure):
    pass
