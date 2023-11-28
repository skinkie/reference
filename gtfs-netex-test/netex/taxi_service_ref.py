from dataclasses import dataclass
from netex.taxi_service_ref_structure import TaxiServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServiceRef(TaxiServiceRefStructure):
    """Identifier of an TAXI SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
