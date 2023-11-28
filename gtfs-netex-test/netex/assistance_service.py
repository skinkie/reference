from dataclasses import dataclass, field
from netex.assistance_service_version_structure import AssistanceServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceService(AssistanceServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE for ASSISTANCE providing information like
    language, accessibility trained staff, etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
