from dataclasses import dataclass, field
from netex.left_luggage_service_version_structure import LeftLuggageServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LeftLuggageService(LeftLuggageServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for left luggage (provides left luggage
    information like self service locker, locker free, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
