from dataclasses import dataclass, field
from netex.service_exclusion_version_structure import ServiceExclusionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceExclusion(ServiceExclusionVersionStructure):
    """A constraint on the use of a service.

    The service, on this specific JOURNEY PATTERN (usually a FTS JOURNEY
    PATTERN) cannot operate when another (regular) service operates.
    This may occur only on subpart of the JOURNEY PATTERN, or only on
    one or some specific SCHEDULED STOP POINTs within the pattern.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
