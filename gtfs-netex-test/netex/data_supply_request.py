from dataclasses import dataclass

from .data_supply_request_structure import DataSupplyRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class DataSupplyRequest(DataSupplyRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
