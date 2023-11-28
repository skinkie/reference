from dataclasses import dataclass, field
from netex.luggage_service_version_structure import LuggageServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageService(LuggageServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for luggage services (provides luggage
    service facilities and characteristics like luggage trolley, free to use,
    etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
