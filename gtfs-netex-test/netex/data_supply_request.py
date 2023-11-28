from dataclasses import dataclass
from netex.data_supply_request_structure import DataSupplyRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class DataSupplyRequest(DataSupplyRequestStructure):
    """Request from Consumer to Producer to fetch update previously notified by a
    Data ready message.

    Answered with a Service Delivery.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
