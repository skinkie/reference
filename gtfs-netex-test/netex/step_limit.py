from dataclasses import dataclass, field
from netex.step_limit_version_structure import StepLimitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StepLimit(StepLimitVersionStructure):
    """
    Geographical parameter limiting the access rights by counts of stops, sections
    or zones.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
