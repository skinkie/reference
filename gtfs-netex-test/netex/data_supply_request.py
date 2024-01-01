from dataclasses import dataclass
from .data_supply_request_structure import DataSupplyRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataSupplyRequest(DataSupplyRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
