from dataclasses import dataclass, field
from netex.special_service_version_structure import SpecialServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecialService(SpecialServiceVersionStructure):
    """A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE.

    The pattern of working is in principle defined by a SERVICE JOURNEY
    PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
