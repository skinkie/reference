from dataclasses import dataclass

from .lines_delivery_structure import LinesDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LinesDelivery(LinesDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
