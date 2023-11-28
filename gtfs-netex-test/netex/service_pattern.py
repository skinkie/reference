from dataclasses import dataclass, field
from netex.service_pattern_version_structure import ServicePatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServicePattern(ServicePatternVersionStructure):
    """
    The subset of a JOURNEY PATTERN made up only of STOP POINTs IN JOURNEY PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
