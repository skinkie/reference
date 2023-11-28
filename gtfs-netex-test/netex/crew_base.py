from dataclasses import dataclass, field
from netex.crew_base_version_structure import CrewBaseVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CrewBase(CrewBaseVersionStructure):
    """
    A place where operating EMPLOYEEs (e.g. drivers) report on and register their
    worK.

    :ivar id: Identifier of a CREW BASE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
