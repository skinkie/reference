from dataclasses import dataclass, field
from netex.tariff_version_structure import TariffVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Tariff(TariffVersionStructure):
    """
    A particular tariff, described by a combination of parameters.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
