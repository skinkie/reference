from dataclasses import dataclass, field
from netex.money_service_version_structure import MoneyServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MoneyService(MoneyServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to money services.

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
