from dataclasses import dataclass

from .organisation_part_ref_structure import OrganisationPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DepartmentRefStructure(OrganisationPartRefStructure):
    pass
