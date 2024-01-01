from dataclasses import dataclass
from .crew_base_version_structure import CrewBaseVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBase(CrewBaseVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
