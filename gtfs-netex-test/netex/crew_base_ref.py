from dataclasses import dataclass
from netex.crew_base_ref_structure import CrewBaseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CrewBaseRef(CrewBaseRefStructure):
    """
    Reference to a CREW BASE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
