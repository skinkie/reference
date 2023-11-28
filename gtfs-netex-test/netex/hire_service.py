from dataclasses import dataclass, field
from netex.hire_service_version_structure import HireServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HireService(HireServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to hire services (e.g. cycle hire,
    car hire).

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
