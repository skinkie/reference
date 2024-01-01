from dataclasses import dataclass
from .crew_base_ref_structure import CrewBaseRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBaseRef(CrewBaseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
