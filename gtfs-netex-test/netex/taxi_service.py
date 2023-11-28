from dataclasses import dataclass, field
from netex.taxi_service_version_structure import TaxiServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiService(TaxiServiceVersionStructure):
    """A type of VEHICLE POOLING SERVICE where the service may be regulated
    according to a particular taxi policy.

    .  +v1.2.2

    :ivar id: Identifier of TAXI SERVICE
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
